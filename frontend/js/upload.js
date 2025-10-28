 /** Initializes drag and drop listeners */
window.onload = function() {

    lucide.createIcons();
    initUploadListeners();
}
function initUploadListeners() {

    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');

    dropZone.onclick = () => fileInput.click();

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, preventDefaults, false);});

    ['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, () => dropZone.classList.add('bg-blue-50'), false);});        // Highlight drop zone on drag enter/over
            
    ['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, () => dropZone.classList.remove('bg-blue-50'), false);});

    dropZone.addEventListener('drop', handleDrop, false);

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        handleFileUpload(files);
    }         
}

const requiredColumns = ["Question","Answer"];
        
function handleFileUpload(files) {
    if (files.length === 0) return;
    
    const file = files[0];
    const fileType = file.name.split('.').pop().toLowerCase();

    // Clear previous error messages
    clearMessages();
    
    // Validate file type and process accordingly
    if (fileType === "csv") {
        parseCSV(file);
    }
    else if (fileType === 'xls' || fileType === 'xlsx') {
        parseExcel(file, fileType);
    }
    else {
        showError("Incorrect file type. Please upload a .csv or .xlsx file.");
    }
}

/** Check if the required columns are present and if they have valid (non-empty) data */
function checkRequiredColumns(columns, rows) {
    const missing = requiredColumns.filter(col => !columns.includes(col));

    if (missing.length > 0) {
        showError(`Missing required columns: ${missing.join(', ')}`);
        disableSubmitButton();
        return;
    }

    // Check if each required column has at least one non-empty, non-null value
    const invalidColumns = requiredColumns.filter(col => {
        const columnData = rows.map(row => row[col]);
        return columnData.every(val => val === null || val.trim() === "");
    });

    if (invalidColumns.length > 0) {
        showError(`The following columns have no valid data: ${invalidColumns.join(', ')}`);
        disableSubmitButton();
    } else {
        showSuccess("File uploaded successfully! All required columns have valid data.");
        enableSubmitButton();
    }
}

/** Parse CSV file */
function parseCSV(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        const csvData = e.target.result;
        Papa.parse(csvData, {
            header: true, // Only parse the header row
            dynamicTyping: true,
            skipEmptyLines: true,
            complete: function(results) {
                const columns = results.meta.fields;
                const rows = results.data;
                checkRequiredColumns(columns, rows);
            },
            error: function(error) {
                showError("Error reading CSV file");
            }
        });
    };
    reader.readAsText(file);
}

/** Parse XLSX or XLS file */
function parseExcel(file, fileType) {
    const reader = new FileReader();
    reader.onload = function(e) {
        const data = e.target.result;
        let workbook;
        
        // Read Excel data
        if (fileType === 'xlsx') {
            workbook = XLSX.read(data, { type: 'binary' });
        } else if (fileType === 'xls') {
            workbook = XLSX.read(data, { type: 'binary', cellDates: true });
        }

        const sheet = workbook.Sheets[workbook.SheetNames[0]]; // Get the first sheet
        const columns = XLSX.utils.sheet_to_json(sheet, { header: 1 })[0]; // Get header row
        const rows = XLSX.utils.sheet_to_json(sheet); // Get all rows
        checkRequiredColumns(columns, rows);
    };
    reader.readAsArrayBuffer(file);
}

function enableSubmitButton() {
    const submitBtn = document.getElementById('submit-analysis-btn');
    submitBtn.disabled = false;
    submitBtn.classList.remove('disabled:opacity-50');
    submitBtn.classList.add('bg-emerald-500');
    document.getElementById('submit-text').textContent = 'Submit for Analysis';
}

function disableSubmitButton() {
    const submitBtn = document.getElementById('submit-analysis-btn');
    submitBtn.disabled = true;
    submitBtn.classList.add('disabled:opacity-50');
    submitBtn.classList.remove('bg-emerald-500');
    document.getElementById('submit-text').textContent = 'Validation Failed: Missing Columns or Empty Data';
}

function showError(message) {
    const errorElement = document.createElement("div");
    errorElement.classList.add("error-message", "bg-red-500", "text-white", "p-4", "mt-4", "rounded");
    errorElement.innerText = message;
    const dropZone = document.getElementById('drop-zone');
    dropZone.insertAdjacentElement('afterend', errorElement);
    //setTimeout(() => errorElement.remove(), 5000);
}

function showSuccess(message) {
    clearMessages();
    const msg = document.createElement("div");
    msg.classList.add("bg-green-500", "text-white", "p-3", "mt-3", "rounded");
    msg.textContent = message;
    document.getElementById('drop-zone').insertAdjacentElement('afterend', msg);
    //setTimeout(() => msg.remove(), 5000);
}

function clearMessages() {
    const existingMessages = document.querySelectorAll('.error-message, .bg-green-500');
    existingMessages.forEach(msg => msg.remove());}

//need to write submitForAnalysis function.