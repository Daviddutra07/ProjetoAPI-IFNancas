const API = "http://localhost:5000/items";

const lista = document.getElementById("lista");
const form = document.getElementById("form");

const filtroTipo = document.getElementById("filtro-tipo");
const filtroStatus = document.getElementById("filtro-status");

const feedback = document.getElementById("feedback");
const loading = document.getElementById("loading");

const resumoEntradas = document.getElementById("resumo-entradas");
const resumoSaidas = document.getElementById("resumo-saidas");
const resumoSaldo = document.getElementById("resumo-saldo");

let editandoId = null;

// Mensagens de aviso
function mostrarFeedback(mensagem, tipo) {
    feedback.className = "p-3 rounded text-sm";

    if (tipo === "erro") {
        feedback.classList.add("bg-red-100", "text-red-700");
    } else {
        feedback.classList.add("bg-green-100", "text-green-700");
    }

    feedback.innerText = mensagem;
    feedback.classList.remove("hidden");

    setTimeout(() => {
        feedback.classList.add("hidden");
    }, 3000);
}

g