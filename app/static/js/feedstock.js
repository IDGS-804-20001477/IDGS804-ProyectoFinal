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
        txtMaxValue.value = txtMinValue.value;
        txtMaxValue.setAttribute('min', txtMinValue.value);
        txtMaxValue.setAttribute('step', txtMinValue.step);
    }
};

const updateQuantity = () => {
    let txtMinValue = document.getElementById('txtMinValue');
    let txtMaxValue = document.getElementById('txtMaxValue');
    let txtQuantity = document.getElementById('txtQuantity');

    if(txtMinValue.value === '' && txtMaxValue.value === ''){
        txtQuantity.value = '';
        txtQuantity.disabled = true;
    }
    else{
        txtQuantity.disabled = false;
        txtQuantity.value = txtMinValue;
        txtQuantity.setAttribute('min', txtMinValue.value);
        txtQuantity.setAttribute('max', txtMaxValue.value);
        txtQuantity.setAttribute('step', txtMaxValue.value);
    }
};