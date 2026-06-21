import {connection_link} from './connection_link.js';

const CL = new connection_link();
const url = CL.getUrl("/ranking");

function renderGlobal(list) {

    if (list.length > 0) {
        const first = list[0];
        document.querySelector(".card-ranking-g.first .username").textContent = first.nick;
        document.querySelector(".card-ranking-g.first .points").textContent = `${first.pontos} pontos`;
    }
    if (list.length > 1) {
        const second = list[1];
        document.querySelector(".card-ranking-g.second .username").textContent = second.nick;
        document.querySelector(".card-ranking-g.second .points").textContent = `${second.pontos} pontos`;
    }
    if (list.length > 2) {
        const third = list[2];
        document.querySelector(".card-ranking-g.third .username").textContent = third.nick;
        document.querySelector(".card-ranking-g.third .points").textContent = `${third.pontos} pontos`;
    }
    const tbody = document.querySelector(".leaderboard-body-global");
    tbody.innerHTML = "";
    list.forEach(user => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${user.posicao}</td>
            <td>${user.nick}</td>
            <td>${user.pontos} pontos</td>
            <td>${user.curso}</td>
        `;
        tbody.appendChild(tr);
    });
}

function renderVersus(list) {
    if (list.length > 0) {
        const first = list[0];
        document.querySelector(".card-ranking-v.first .username").textContent = first.nick;
        document.querySelector(".card-ranking-v.first .points").textContent = `${first.pontos} pontos`;
    }
    if (list.length > 1) {
        const second = list[1];
        document.querySelector(".card-ranking-v.second .username").textContent = second.nick;
        document.querySelector(".card-ranking-v.second .points").textContent = `${second.pontos} pontos`;
    }
    if (list.length > 2) {
        const third = list[2];
        document.querySelector(".card-ranking-v.third .username").textContent = third.nick;
        document.querySelector(".card-ranking-v.third .points").textContent = `${third.pontos} pontos`;
    }
    const tbody = document.querySelector(".leaderboard-body-versus");
    tbody.innerHTML = "";
    list.forEach(user => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${user.posicao}</td>
            <td>${user.nick}</td>
            <td>${user.pontos} pontos</td>
            <td>${user.curso}</td>
        `;
        tbody.appendChild(tr);
    });
}

async function loadLeaderboard() {

    try {

        const response = await fetch(url);
        const data = await response.json();

        console.log(data);

        renderGlobal(data.global || []);
        renderVersus(data.versus || []);

    } catch (error) {

        console.error("Erro ao carregar leaderboard:", error);
    }
}

loadLeaderboard();