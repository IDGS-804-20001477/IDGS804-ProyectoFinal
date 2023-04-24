const updateMinValue = () => {
    let cmbMeasurement_unit = document.getElementById('cmbMeasurement_unit').value;
    console.log(cmbMeasurement_unit);
    let txtMinValue = document.getElementById('txtMinValue');

    if(cmbMeasurement_unit === "1"){
        txtMinValue.step = 1
        txtMinValue.disabled = false
    }
    else if( cmbMeasurement_unit === "2"){
        txtMinValue.step = 0.01;
        txtMinValue.disabled = false;
    }
};

const updateMaxValue = () => {
    let txtMinValue = document.getElementById('txtMinValue')
    let txtMaxValue = document.getElementById('txtMaxValue');

    if(txtMinValue.value === ''){
        txtMaxValue.value = '';
        txtMaxValue.disabled = true;
    }
    else{
        txtMaxValue.disabled = false;
        txtMaxValue.min = txtMinValue.min;
        txtMaxValue.value = txtMinValue.value;
        txtMaxValue.step = txtMinValue.step;
    }
};

const updateQuantity = () => {
    let txtMinValue = document.getElementById('txtMinValue').value;
    let txtMaxValue = document.getElementById('txtMaxValue');
    let txtQuantity = document.getElementById('txtQuantity');

    if(txtMinValue === '' && txtMaxValue.value === ''){
        txtQuantity.value = '';
        txtQuantity.disabled = true;
    }
    else{
        txtQuantity.disabled = false;
        txtQuantity.min = txtMinValue;
        txtQuantity.max = txtMaxValue
        txtQuantity.value = txtMinValue;
        txtQuantity.step = txtMaxValue.step;
    }
};