
const dadosDesempenho = [
{ area: "Álgebra Linear", nivel: "Avançado", valor: 80 },
{ area: "Cálculo Diferencial", nivel: "Intermediário", valor: 50 },
{ area: "Cálculo Integral", nivel: "Avançado", valor: 70 },
{ area: "Equação Polinomial de 2 Grau", nivel: "Intermediário", valor: 40 }
];

const container = document.getElementById("grafico-container");

dadosDesempenho.forEach(item => {
    const divArea = document.createElement("div");
    divArea.style.marginBottom = "15px";
    const texto = document.createElement("p");
    texto.innerHTML = `<strong>${item.area}</strong> - <span>${item.nivel}</span>`;
            
    const barra = document.createElement("progress");
    barra.max = 100;
    barra.value = item.valor;
    barra.style.width = "100%";

    divArea.appendChild(texto);
    divArea.appendChild(barra);
    container.appendChild(divArea);
});