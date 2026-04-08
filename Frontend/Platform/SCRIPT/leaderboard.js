console.log("ta funfando");

import {connection_link} from './connection_link.js';

const CL = new connection_link();
const url = CL.getUrl("/ranking");

console.log("ta funfando");
/*
async function top3ranking() {
    try {
        const response = await fetch(url);
        const list = await response.json();

        list.forEach((user, index) => {
            if (index < 3) {

            }
        })
    } catch (error) {
        console.log("Erro ao carregar top 3 do ranking:", error);
    }
}
*/

async function loadLeaderboard() {
    try {
        const response = await fetch(url);
        const list = await response.json();

        const tbody = document.querySelector(".leaderboard-table tbody");
        tbody.innerHTML = "";

        list.forEach((user) => {
            const tr = document.createElement("tr");

            tr.innerHTML = `
                <td>${user.posicao}</td>
                <td>${user.nick}</td>
                <td>${user.pontos} pontos</td>
                <td>${user.curso}</td>
            `;

            tbody.appendChild(tr);
        });

    } catch (error) {
        console.log("Erro ao carregar leaderboard:", error);
    }
}

loadLeaderboard();