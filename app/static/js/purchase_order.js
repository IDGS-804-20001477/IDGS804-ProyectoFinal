const insertDataDetail = () => {
    let provider = document.getElementById('cmbProvider').value;
    let _name = document.getElementById('cmbProvider');
    let feedstock = document.getElementById('cmbFeedstocks').value;
    let name = document.getElementById('cmbFeedstocks');
    let text = name.options[name.selectedIndex].innerHTML;
    let _text = _name.options[_name.selectedIndex].innerHTML;
    let quantity = document.getElementById('txtQuantity').value;
    let price = document.getElementById('txtPrice').value;

    document.getElementById('tBodyDetails').innerHTML += "<tr><td>" + feedstock + "</td><td>" + text + "</td><td>" + quantity + "</td><td><input type='button' value='Delete' class='btn btn-danger'></td></tr>";

    document.getElementById('txtQuantity').value = '';
    _name.focus();
};

const insertRecipe = () => {
    let table = $('table tbody');
    let data = [];
    let product_id = document.getElementById('cmbProducts').value;
    let description = document.getElementById('txtDescription').value;
    let token = document.getElementById('csrf_token').value;

    table.find('tr').each(function (i) {
        let object = { "feedstock_id": 0, "quantity": 0.0 };
        let $tds = $(this).find('td'),
            feedstock_id = $tds.eq(0).text(),
            quantity = $tds.eq(2).text();

        object.feedstock_id = parseInt(feedstock_id);
        object.quantity = parseFloat(quantity);
        data.push(object);
    });

    fetch('http://127.0.0.1:5000/admin/recipes/recipes-insert', {
        method: 'POST',
        body: JSON.stringify({
            product_id: product_id,
            description: description,
            array: JSON.stringify(data)
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
            'X-CSRF-Token': token
        }
    });
};

const deleteRow = (row) => {
    document.getElementById('tblDetail').deleteRow(row);
};

const tableClick = (e) => {
    if (!e) {
        e = window.event;
    }

    if (e.target.value === "Delete") {
        deleteRow(e.target.parentNode.parentNode.rowIndex);
    }
};

window.onload = function () {
    document.getElementById('tblDetail').addEventListener('click', tableClick, false);
};