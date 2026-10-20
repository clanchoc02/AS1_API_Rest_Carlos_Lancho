document.getElementById("formulario").addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const datos = {
        modelo: document.getElementById("modelo").value,
        anio: parseInt(document.getElementById("anio").value),
        km: parseInt(document.getElementById("km").value),
        precio_nuevo: parseFloat(document.getElementById("precio_nuevo").value),
        unico_dueno: document.getElementById("unico_dueno").checked
    };

    const res = await fetch("http://127.0.0.1:8000/tasar-coche", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(datos)
    });

    const json = await res.json();
    
    if (res.ok) {
        document.getElementById("precio").textContent = json.precio_estimado + " €";
        document.getElementById("valoracion").textContent = json.valoracion;
        document.getElementById("explicacion").textContent = json.explicacion;
        document.getElementById("resultado").classList.remove("hidden");
    } else {
        alert("Error en los datos enviados");
    }
});