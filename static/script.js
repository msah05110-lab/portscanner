async function scanPorts() {

    let ip = document.getElementById("ip").value;

    if(ip.trim() === ""){
        alert("Enter IP or Domain");
        return;
    }

    document.getElementById("results").innerHTML = `
        <div class="loading-box">
            <h3>Scanning Target...</h3>
        </div>
    `;

    let response = await fetch("/scan", {
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            ip:ip
        })
    });

    let data = await response.json();

    let html = `
        <div class="result-card">

        <h2>Scan Results</h2>

        <table class="table table-bordered table-hover">

        <thead>
            <tr>
                <th>Port</th>
                <th>Service</th>
            </tr>
        </thead>

        <tbody>
    `;

    data.forEach(item => {

        html += `
            <tr>
                <td>${item.port}</td>
                <td>${item.service}</td>
            </tr>
        `;
    });

    html += `
        </tbody>
        </table>
        </div>
    `;

    document.getElementById("results").innerHTML = html;
}