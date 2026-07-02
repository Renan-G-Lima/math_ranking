document.querySelectorAll(".toggle-group").forEach(group => {
    const tabs = group.querySelectorAll(".ranking-tab");

    tabs.forEach(tab => {
        tab.addEventListener("click", () => {
            tabs.forEach(t => t.classList.remove("active"));
            group.querySelectorAll(".ranking-panel").forEach(p => p.classList.remove("active"));

            tab.classList.add("active");
            group.querySelector(`[data-panel="${tab.dataset.target}"]`).classList.add("active");
        });
    });
});