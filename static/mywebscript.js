const RunSentimentAnalysis = () => {
    const textToAnalyze =
        document.getElementById("textToAnalyze").value;

    const responseElement =
        document.getElementById("system_response");

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            responseElement.textContent = this.responseText;
        }
    };

    const endpoint =
        "/emotionDetector?textToAnalyze=" +
        encodeURIComponent(textToAnalyze);

    xhttp.open("GET", endpoint, true);
    xhttp.send();
};
