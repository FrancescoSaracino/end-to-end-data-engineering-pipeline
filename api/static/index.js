let prodottiGlobali = [];
let paginaCorrente = 1;
const perPagina = 5; // numero di prodotti per pagina

// FETCH API
fetch("/amazon/elenco")
.then(res => res.json())
.then(data => {
    prodottiGlobali = data;
    renderPagina(paginaCorrente);
})
.catch(err => console.error("Errore fetch:", err));

function renderPagina(pagina) {
    paginaCorrente = pagina;
    const start = (paginaCorrente - 1) * perPagina;
    const end = start + perPagina;
    const subset = prodottiGlobali.slice(start, end);

    creaTabella(subset);
    creaCards(subset);
    renderPagination();

    // Scroll dolce in cima alla tabella
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function creaTabella(prodotti) {
    const thead = document.querySelector("#amazon-table thead");
    const tbody = document.querySelector("#amazon-table tbody");

    thead.innerHTML = "";
    tbody.innerHTML = "";

    if (!prodotti || prodotti.length === 0) {
        thead.innerHTML = "<tr><th>Nessun dato disponibile</th></tr>";
        return;
    }

    const colonne = ["id_prodotto","categoria","conteggio_valutazioni","contenuto_recensione","descrizione_prodotto"];
    thead.innerHTML = `<tr>${colonne.map(c => `<th>${c}</th>`).join("")}</tr>`;

    prodotti.forEach(p => {
        const riga = colonne.map(c => `<td class="truncate">${p[c] ?? ""}</td>`).join("");
        tbody.innerHTML += `<tr>${riga}</tr>`;
    });
}

function creaCards(prodotti) {
    const container = document.getElementById("cards-container");
    container.innerHTML = "";

    if (!prodotti || prodotti.length === 0) {
        container.innerHTML = "<p>Nessun prodotto</p>";
        return;
    }

    prodotti.forEach(p => {
        const stelle = creaStelle(p.valutazione_media);
        const sconto = p.percentuale_sconto ? `<span class="badge-sconto">-${p.percentuale_sconto}%</span>` : "";

        container.innerHTML += `
            <div class="card">
                <img src="${p.link_immagine ?? ''}" alt="Immagine prodotto">
                <h3>${p.nome_prodotto ?? ''}</h3>
                <p><i class="fa-solid fa-tag"></i> ${p.categoria ?? ''}</p>
                <p class="prezzi">
                  <strong class="prezzo-scontato">${p.prezzo_scontato ?? ''} €</strong>
                  ${p.prezzo_originale ? `<span class="prezzo-originale">${p.prezzo_originale} €</span>` : ''}
                </p>
                ${sconto}
                <p class="stelle">${stelle}</p>
            </div>
        `;
    });

    // Setta il click sulle card
    setupCardClick();
}

// Funzione helper per creare stelle
function creaStelle(valutazione) {
    valutazione = Math.round(valutazione ?? 0);
    let html = "";
    for (let i = 0; i < 5; i++) {
        if (i < valutazione) html += '<i class="fa-solid fa-star" style="color:gold;"></i>';
        else html += '<i class="fa-regular fa-star" style="color:#ccc;"></i>';
    }
    return html;
}

// Imposta click sulle card per aprire il modal
function setupCardClick() {
    document.querySelectorAll(".card").forEach((card, index) => {
        card.onclick = () => {
            const prodotto = prodottiGlobali[(paginaCorrente-1)*perPagina + index];
            apriModal(prodotto);
        };
    });
}

// PAGINAZIONE
function renderPagination() {
    const container = document.getElementById("pagination");
    container.innerHTML = "";

    const totalPagine = Math.ceil(prodottiGlobali.length / perPagina);

    if (paginaCorrente > 1) {
        const prev = document.createElement("button");
        prev.textContent = "Back";
        prev.onclick = () => renderPagina(paginaCorrente - 1);
        container.appendChild(prev);
    }

    if (paginaCorrente < totalPagine) {
        const next = document.createElement("button");
        next.textContent = "Next";
        next.onclick = () => renderPagina(paginaCorrente + 1);
        container.appendChild(next);
    }
}

// MODAL
function apriModal(prodotto) {
    document.getElementById("modal-nome").textContent = prodotto.nome_prodotto ?? "";
    document.getElementById("modal-categoria").textContent = prodotto.categoria ?? "";
    document.getElementById("modal-prezzo").textContent = prodotto.prezzo_scontato ?? "";
    document.getElementById("modal-valutazione").textContent = prodotto.valutazione_media ?? "";
    document.getElementById("modal-conteggio").textContent = prodotto.conteggio_valutazioni ?? "";
    document.getElementById("modal-descrizione").textContent = prodotto.descrizione_prodotto ?? "";
    document.getElementById("modal-recensione").textContent = prodotto.contenuto_recensione ?? "";
    document.getElementById("modal-immagine").src = prodotto.link_immagine ?? "";

    document.getElementById("product-modal").style.display = "block";
}

// Chiusura modal
document.getElementById("close-modal").onclick = () => {
    document.getElementById("product-modal").style.display = "none";
}

window.onclick = (event) => {
    const modal = document.getElementById("product-modal");
    if (event.target == modal) modal.style.display = "none";
}
