import {connection_link} from './connection_link.js';

const CL = new connection_link();
const url = CL.getUrl("/ranking");

async function loadLeaderboard() {
    try {
        const response = await fetch(url);
        const list = await response.json();

        if (list.length >= 3) {
            const first = list[0];
            const second = list[1];
            const third = list[2];

            document.querySelector(".card-ranking.first .username").textContent = first.nick;
            document.querySelector(".card-ranking.first .points").textContent = `${first.pontos} pontos`;

            document.querySelector(".card-ranking.second .username").textContent = second.nick;
            document.querySelector(".card-ranking.second .points").textContent = `${second.pontos} pontos`;

            document.querySelector(".card-ranking.third .username").textContent = third.nick;
            document.querySelector(".card-ranking.third .points").textContent = `${third.pontos} pontos`;
        }

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