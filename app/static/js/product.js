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