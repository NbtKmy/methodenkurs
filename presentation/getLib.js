function getBib(a, b){
    let itemSet = "";
    
    for (var i = 0; i < a.length; i++) {

        
        
        const bool = a[i].data.tags.some(
            d => d.tag === b
            );
        
        if (bool){
            iType = a[i].data.itemType

            if (iType == 'book'){
                let title = a[i].data.title;
                let y = a[i].data.date;
                let year = y.substring(0, 4);
                let place = a[i].data.place;
                let pub = a[i].data.publisher;

                if (a[i].data.creators != 0) {
                    var creators = "";
                    for (var j = 0; j < a[i].data.creators.length; j++){
                        let pers = a[i].data.creators[j].lastName + ", " + a[i].data.creators[j].firstName;
                        if (creators.length == 0){
                        creators = creators + pers;
                        }
                        else {
                        creators = creators.concat("; ", pers);
                        }
                    }
                }
                var itm = creators + '. (' + year + ') ' + title + '. ' + place + ', ' + pub + '.';
            }
            else if (iType == 'journalArticle'){
                let title = a[i].data.title;
                let y = a[i].data.date;
                let year = y.substring(0, 4);
                let journalTit = a[i].data.publicationTitle;
                let vol = a[i].data.volume;
                let iss = a[i].data.issue;
                let pg = a[i].data.pages;

                if (a[i].data.creators != 0) {
                    var creators = "";
                    for (var j = 0; j < a[i].data.creators.length; j++){
                        let pers = a[i].data.creators[j].lastName + ", " + a[i].data.creators[j].firstName;
                        if (creators.length == 0){
                        creators = creators + pers;
                        }
                        else {
                        creators = creators.concat("; ", pers);
                        }
                    }
                }
                var itm = creators + '. (' + year + ') "' + title + '". In: ' + journalTit +'. ' + vol + '(' + iss + '),  pp.' + pg + '.';
            }
            else if (iType == 'webpage'){
                let title = a[i].data.title;
                let y = a[i].data.accessDate;
                let year = y.substring(0, 10);
                let url = a[i].data.url;
                
                if (a[i].data.creators != 0) {
                    var creators = "";
                    for (var j = 0; j < a[i].data.creators.length; j++){
                        let pers = a[i].data.creators[j].lastName + ", " + a[i].data.creators[j].firstName;
                        if (creators.length == 0){
                        creators = creators + pers;
                        }
                        else {
                        creators = creators.concat("; ", pers);
                        }
                    }
                }
                var itm = creators + '. ' + title + '. ' + url + '. Accessed: ' + year;
            }
            itemSet = itemSet + "<p>" + itm + "</p>"
            }
        }
    return itemSet
};

function getLib(){ 
    fetch('https://api.zotero.org/groups/2362804/collections/QKPDUIKW/items?format=json').then(function(response) {
        return response.json();
})
.then(function(json){

    itemSet = getBib(json, "jpn");
    el = document.getElementById("output");
    el.innerHTML = itemSet;

    itemSet2 = getBib(json, "wfl");
    el2 = document.getElementById("output2");
    el2.innerHTML = itemSet2;

    itemSet3 = getBib(json, "wfl2");
    el3 = document.getElementById("output3");
    el3.innerHTML = itemSet3;

    console.log(json);
    
})
};