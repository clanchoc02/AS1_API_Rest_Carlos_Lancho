document.getElementById("formulario").addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const datos = {
        modelo: document.getElementById("modelo").value,
        anio: parseInt(document.getElementById("anio").value),
        km: parseInt(document.getElementById("km").value),
        precio_nuevo: parseFloat(document.getElementById("precio_nuevo").value),
        unico_dueno: document.getElementById("unico_dueno").checked
    };

    try {
        // Usar ruta relativa "/tasar-coche" para que funcione tanto en local como en Render
        const res = await fetch("/tasar-coche", {
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
            alert("Error en los datos enviados: " + (json.detail || "Verifica los campos"));
        }
    } catch (error) {
        console.error("Error al conectar con la API:", error);
        alert("No se pudo conectar con el servidor. Si acabas de abrir la web, Render puede tardar unos 40 segundos en despertar.");
    }
});
