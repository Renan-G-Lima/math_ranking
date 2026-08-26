const areasData = [
    { label: "Cálculo Integral", valor: 35, cor: "#00e000" },
    { label: "Álgebra Linear", valor: 28, cor: "#00c100" },
    { label: "Equações", valor: 22, cor: "#009c00" },
    { label: "Outras", valor: 15, cor: "#3a3a3a" }
];

const donut = document.getElementById("areas-donut");
const legend = document.getElementById("areas-legend");

let acumulado = 0;
const fatias = areasData.map(item => {
    const inicio = acumulado;
    acumulado += item.valor;
    return `${item.cor} ${inicio}% ${acumulado}%`;
});

donut.style.background = `conic-gradient(${fatias.join(", ")})`;

areasData.forEach(item => {
    const li = document.createElement("li");
    li.innerHTML = `<span class="legend-dot" style="background-color:${item.cor}"></span>${item.label} <b>${item.valor}%</b>`;
    legend.appendChild(li);
});