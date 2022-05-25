function deafGrandma(count = 0) {
    let input = prompt('HEY KID!')
    if(input === ''){
        alert('WHAT?!');
    } else if(input === "GOODBYE!" && count === 0){
        alert('LEAVING SO SOON?')
        return deafGrandma(1);
    } else if(input === "GOODBYE!" && count === 1){
        alert('LATER, SKATER!')
        return;
    } else if(input === input.toUpperCase()){
        alert('NO, NOT SINCE 1946!');
    } else {
        alert('SPEAK UP, KID!');
    }
     deafGrandma(count)
}

deafGrandma();