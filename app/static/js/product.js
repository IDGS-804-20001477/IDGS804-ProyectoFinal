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