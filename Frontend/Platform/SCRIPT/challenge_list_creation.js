function createItemOnList(ID, name, finished){
    const listElement = document.querySelector('._challenge_list');
    
    const item = document.createElement('div');
    item.classList.add('_challenge_list-item');
    item.id = ID;
    item.setAttribute('onmouseover','summaryChanger(this)');
    
    const challenge = document.createElement('p');
    challenge.id = "challenge";
    challenge.textContent = name;

    const status = document.createElement('p');
    status.id = "status";
    status.textContent = finished;

    item.appendChild(challenge);
    item.appendChild(status);

    listElement.appendChild(item);
}

const descriptions = {
    I001: "A soma, também conhecida como adição, é uma das quatro operações fundamentais da aritmética. Ela consiste na união ou combinação de dois ou mais valores (chamados de parcelas) para formar um total único, denominado soma ou total.",
    I002: "Alterando para outra descrição"
}

function summaryChanger(element){
    const elementName = element.id;
    const temporaryDescription = descriptions[elementName];
    const description = document.querySelector('#descricao');
    description.textContent = temporaryDescription;
}

createItemOnList('I001', 'Descrição da Soma', false);
createItemOnList('I002', 'Outra Descrição', false);