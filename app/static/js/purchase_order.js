/*
const insertDataDetail = () => {
    let feedstock = document.getElementById('cmbFeedstocks').value;
    let name = document.getElementById('cmbFeedstocks');
    let text = name.options[name.selectedIndex].innerHTML;
    let quantity = document.getElementById('txtQuantity').value;
    let price = document.getElementById('txtPrice').value;
    let table = $('table tbody');

    document.getElementById('tBodyDetails').innerHTML += "<tr><td>" + feedstock + "</td><td>" + text + "</td><td>" + quantity + "</td><td>" + price + "</td><td><input type='button' value='Delete' class='btn btn-danger'></td></tr>";

    document.getElementById('txtQuantity').value = '';
    document.getElementById('txtPrice').value = '';
    name.focus();

    let total = 0;
    table.find('tr').each(function (i) {
        let $tds = $(this).find('td'),
            price = $tds.eq(3).text(),
            quantity = $tds.eq(2).text();

        total = total + (parseInt(price) * parseInt(quantity));
    });

    document.getElementById('txtTotal').value = total;
};

const insertPurchaseOrder = () => {
    let table = $('table tbody');
    let data = [];
    let provider_id = document.getElementById('cmbProvider').value;
    let total = document.getElementById('txtTotal').value;
    let token = document.getElementById('csrf_token').value;

    table.find('tr').each(function (i) {
        let object = { "quantity": 0.0, "price": 0.0, "feedstock_id": 0 };
        let $tds = $(this).find('td'),
            feedstock_id = $tds.eq(0).text(),
            quantity = $tds.eq(2).text(),
            price = $tds.eq(3).text();

        object.feedstock_id = parseInt(feedstock_id);
        object.quantity = parseFloat(quantity);
        object.price = parseFloat(price)
        data.push(object);
    });

    fetch('http://127.0.0.1:5000/admin/purchase-orders/purchase-orders-insert', {
        method: 'POST',
        body: JSON.stringify({
            provider_id: provider_id,
            total: total,
            array: JSON.stringify(data)
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
            'X-CSRF-Token': token
        }
    }).then((response) => {
        response.json().then((data) => {
            console.log(data);
        });
    });
};

const getFeedstocksByProvider = (select) => {
    let provider_id = select.value;
    let token = document.getElementById('csrf_token').value;
    let cmbFeedstocks = document.getElementById('cmbFeedstocks');

    fetch('http://127.0.0.1:5000/admin/feedstocks/feedstocks-by-provider', {
        method: 'POST',
        body: JSON.stringify({
            id: provider_id
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
            'X-CSRF-Token': token
        }
    }).then((response) => {
        response.json().then((data) => {

            data.forEach((object) => {
                let opt = document.createElement('option')
                opt.value = object.id;
                opt.innerHTML = object.name;
                cmbFeedstocks.append(opt);
            });
        });
    });
}

const deleteRow = (row) => {
    document.getElementById('tblDetail').deleteRow(row);
    let table = $('table tbody');
    let total = 0;
    table.find('tr').each(function (i) {
        let $tds = $(this).find('td'),
            price = $tds.eq(3).text(),
            quantity = $tds.eq(2).text();

        total = total + (parseInt(price) * parseInt(quantity));
    });
    document.getElementById('txtTotal').value = total;
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
*/