let voiceRisk = "LOW";
let textRisk = "LOW";
let imageRisk = "LOW";

function getRiskColor(risk){

    if(risk === "LOW") return "#22c55e";
    if(risk === "MEDIUM") return "#f59e0b";

    return "#ef4444";
}

function createRiskBadge(risk){

    return `
    <div style="
        background:${getRiskColor(risk)};
        color:white;
        padding:10px;
        border-radius:10px;
        text-align:center;
        font-weight:bold;
        margin-top:10px;
    ">
        ${risk}
    </div>
    `;
}

function scrollToResult(id){

    document
        .getElementById(id)
        .scrollIntoView({
            behavior:"smooth",
            block:"center"
        });
}

function updateMeter(level){

    const meter =
        document.getElementById("meterFill");

    if(level === "LOW"){

        meter.style.width = "30%";
        meter.style.background = "#22c55e";
    }

    else if(level === "MEDIUM"){

        meter.style.width = "65%";
        meter.style.background = "#f59e0b";
    }

    else{

        meter.style.width = "100%";
        meter.style.background = "#ef4444";
    }
}

function showLoading(id){

    document.getElementById(id).innerHTML =
    `<div class="loader"></div>`;
}

window.onload = () => {

    console.log(
        "SentinelAI Cyber Defense Center Activated"
    );

};

async function analyzeVoice(){

    const file =
        document.getElementById("voiceFile").files[0];

    if(!file){
        alert("Please select a voice file");
        return;
    }

    showLoading("voiceResult");

    const formData = new FormData();
    formData.append("file", file);

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/analyze-voice",
            {
                method:"POST",
                body:formData
            }
        );

        const data = await response.json();

        voiceRisk = data.risk_level;

    document.getElementById("voiceResult").innerHTML =
`
    <h3>🎤 Voice Analysis Result</h3>

    ${createRiskBadge(data.risk_level)}
`   ;

scrollToResult("voiceResult");    

    }catch(error){

        document.getElementById("voiceResult").innerHTML =
        "Error analyzing voice.";
    }
}

async function analyzeText(){

    const text =
        document.getElementById("textInput").value;

    if(!text){
        alert("Please enter text");
        return;
    }

    showLoading("textResult");

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/analyze-text",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    text:text
                })
            }
        );

        const data = await response.json();

        textRisk = data.risk_level;

        document.getElementById("textResult").innerHTML =
`
<h3>💬 Text Analysis Result</h3>

${createRiskBadge(data.risk_level)}
`;

scrollToResult("textResult");

    }catch(error){

        document.getElementById("textResult").innerHTML =
        "Error analyzing text.";
    }
}

async function analyzeCurrency(){

    const file =
        document.getElementById("currencyFile").files[0];

    if(!file){
        alert("Please select a currency image");
        return;
    }

    showLoading("currencyResult");

    const formData = new FormData();
    formData.append("file", file);

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/analyze-currency",
            {
                method:"POST",
                body:formData
            }
        );

        const data = await response.json();
        if(data.prediction === "Likely Genuine Currency"){
    imageRisk = "LOW";
}
else if(data.prediction === "Possibly Genuine Currency"){
    imageRisk = "MEDIUM";
}
else if(data.prediction === "Not a Currency"){
    imageRisk = "HIGH";
}
else{
    imageRisk = "HIGH";
}
document.getElementById("currencyResult").innerHTML =
`
<h3>💵 Currency Analysis Result</h3>

<p>
<b>Prediction:</b>
${data.prediction}
</p>

<p>
<b>Confidence:</b>
${data.confidence}%
</p>

<p>
<b>Mean Intensity:</b>
${data.mean_intensity}
</p>

<p>
<b>Edge Density:</b>
${data.edge_density}
</p>

<p>
<b>Texture Score:</b>
${data.texture_score}
</p>

${createRiskBadge(imageRisk)}
`;

scrollToResult("currencyResult");

    }catch(error){

        document.getElementById("currencyResult").innerHTML =
        "Error analyzing currency.";
    }
}

async function analyzeFace(){

    const file =
        document.getElementById("faceFile").files[0];

    if(!file){
        alert("Please select a face image");
        return;
    }

    showLoading("faceResult");

    const formData = new FormData();
    formData.append("file", file);

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/analyze-face",
            {
                method:"POST",
                body:formData
            }
        );

        const data = await response.json();
        if(data.prediction.includes("Fake")){
    imageRisk = "HIGH";
}
else{
    imageRisk = "LOW";
}
        document.getElementById("faceResult").innerHTML =
`
<h3>👤 Face Analysis Result</h3>

<p>
<b>Prediction:</b>
${data.prediction}
</p>

<p>
<b>Confidence:</b>
${data.confidence}%
</p>
`;

    }catch(error){

        document.getElementById("faceResult").innerHTML =
        "Error analyzing face.";
    }
}

async function calculateThreat(){

    showLoading("finalResult");

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/citizen-fraud-shield",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    voice_risk:voiceRisk,
                    text_risk:textRisk,
                    image_risk:imageRisk
                })
            }
        );

        const data = await response.json();

        updateMeter(data.final_threat);

       document.getElementById("finalResult").innerHTML =
`
       <h2 style="
       color:${getRiskColor(data.final_threat)};
       margin-bottom:10px;
    ">🚨 ${data.final_threat}
     </h2>

${createRiskBadge(data.final_threat)}

<p style="
margin-top:15px;
line-height:1.6;
">
${data.recommendation}
</p>
`;

scrollToResult("finalResult");

    }catch(error){

        document.getElementById("finalResult").innerHTML =
        "Error calculating threat.";
    }
}

async function analyzeNetwork(){

    showLoading("networkResult");

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/analyze-network"
        );

        const data = await response.json();

        document.getElementById("networkResult").innerHTML =
        `
        <b>Top Suspect:</b> ${data.top_suspect}<br>
        <b>Total Nodes:</b> ${data.total_nodes}<br>
        <b>Connections:</b> ${data.total_connections}
        `;

    }catch(error){

        document.getElementById("networkResult").innerHTML =
        "Error loading network.";
    }
}

async function loadCrimeHotspots(){

    showLoading("crimeResult");

    try{

        const response = await fetch(
            "http://127.0.0.1:8000/crime-hotspots"
        );

        const data = await response.json();

        document.getElementById("crimeResult").innerHTML =
        `
        <b>Highest Risk City:</b> ${data.highest_risk_city}<br>
        <b>Cases:</b> ${data.cases}
        `;

    }catch(error){

        document.getElementById("crimeResult").innerHTML =
        "Error loading hotspots.";
    }
}
function downloadReport(){

    window.open(
        "http://127.0.0.1:8000/download-report",
        "_blank"
    );

}
