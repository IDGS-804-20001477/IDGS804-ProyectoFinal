const insertDataRecipeDetail = () => {
    let feedstock = document.getElementById('cmbFeedstocks').value;
    let name = document.getElementById('cmbFeedstocks');
    let text = name.options[name.selectedIndex].innerHTML;
    let quantity = document.getElementById('txtQuantity').value;

    document.getElementById('tBodyDetails').innerHTML += "<tr><td>" + feedstock + "</td><td>" + text + "</td><td>" + quantity + "</td><td>2</td></tr>";

    document.getElementById('txtQuantity').value = '';
    name.focus();
};

const insertRecipe = () => {
    let table = $('table tbody');
    let data = [];
    let product_id = document.getElementById('cmbProducts').value;
    let description = document.getElementById('txtDescription').value;
    let token = document.getElementById('csrf_token').value;
    
    table.find('tr').each(function(i) {
        let object = {"feedstock_id": 0, "quantity": 0.0};
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
        headers:{
            'Content-type': 'application/json; charset=UTF-8',
            'X-CSRF-Token': token
        }
    });
};