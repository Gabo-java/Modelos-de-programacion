// Obtener parámetros de la URL
const params = new URLSearchParams(window.location.search);
const raza = params.get("raza");

async function cargarRaza() {
  const contenedor = document.getElementById("detalle");
  if (!raza) {
    contenedor.innerHTML = "<h2 class='text-danger'>⚠️ No se seleccionó ninguna raza.</h2>";
    return;
  }

  try {
    const response = await fetch(`/api/seleccionar/${raza}`);
    if (!response.ok) {
      contenedor.innerHTML = `<h2 class="text-danger">❌ Raza "${raza}" no encontrada</h2>`;
      return;
    }

    const data = await response.json();
    contenedor.innerHTML = `
      <div class="card mx-auto" style="max-width: 400px;">
        <img src="/static/img/${raza}.jpg" class="card-img-top" alt="${data.raza}">
        <div class="card-body bg-dark text-light">
          <h2 class="card-title">${data.raza.toUpperCase()}</h2>
          <p class="card-text">🗡️ Arma: ${data.arma}</p>
          <p class="card-text">🛡️ Armadura: ${data.armadura}</p>
          <p class="card-text">💪 Cuerpo: ${data.cuerpo}</p>
          <p class="card-text">🐎 Montura: ${data.montura}</p>
        </div>
      </div>
    `;
  } catch (error) {
    console.error("Error:", error);
    contenedor.innerHTML = "<h2 class='text-danger'>❌ Error al cargar los datos.</h2>";
  }
}

cargarRaza();
