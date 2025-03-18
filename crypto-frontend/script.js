document.addEventListener("DOMContentLoaded", function () {
    const script = document.createElement("script");
    script.src = "https://s3.tradingview.com/tv.js";
    script.async = true;
    script.onload = () => loadChart("BTCUSDT"); 
    document.body.appendChild(script);

    document.querySelectorAll(".tab-btn").forEach(button => {
        button.addEventListener("click", function () {
            document.querySelector(".tab-btn.active").classList.remove("active");
            this.classList.add("active");
            loadChart(this.getAttribute("data-crypto"));
        });
    });

    function loadChart(symbol) {
        document.getElementById("tradingview_chart").innerHTML = "";  
        new TradingView.widget({
            container_id: "tradingview_chart",
            width: "100%",
            height: "500",
            symbol: `BINANCE:${symbol}`,
            interval: "1",
            theme: "dark",
            locale: "en",
            toolbar_bg: "#f1f3f6",
            enable_publishing: false,
        });
    }
});
document.addEventListener("DOMContentLoaded", function () {
    const script = document.createElement("script");
    script.src = "https://s3.tradingview.com/tv.js";
    script.async = true;
    script.onload = () => loadChart("BTCUSDT"); 
    document.body.appendChild(script);

    document.querySelectorAll(".tab-btn").forEach(button => {
        button.addEventListener("click", function () {
            document.querySelector(".tab-btn.active").classList.remove("active");
            this.classList.add("active");
            loadChart(this.getAttribute("data-crypto"));
        });
    });

    function loadChart(symbol) {
        document.getElementById("tradingview_chart").innerHTML = "";  
        new TradingView.widget({
            container_id: "tradingview_chart",
            width: "100%",
            height: "500",
            symbol: `BINANCE:${symbol}`,
            interval: "1",
            theme: "dark",
            locale: "en",
            toolbar_bg: "#f1f3f6",
            enable_publishing: false,
        });
    }
});
document.addEventListener("DOMContentLoaded", function () {
    // Load TradingView Script
    const script = document.createElement("script");
    script.src = "https://s3.tradingview.com/tv.js";
    script.async = true;
    script.onload = () => loadChart("BTCUSDT");
    document.body.appendChild(script);

    // Tab Switch for Cryptos
    document.querySelectorAll(".tab-btn").forEach(button => {
        button.addEventListener("click", function () {
            document.querySelector(".tab-btn.active").classList.remove("active");
            this.classList.add("active");
            loadChart(this.getAttribute("data-crypto"));
        });
    });

    function loadChart(symbol) {
        document.getElementById("tradingview_chart").innerHTML = "";
        new TradingView.widget({
            container_id: "tradingview_chart",
            width: "100%",
            height: "500",
            symbol: `BINANCE:${symbol}`,
            interval: "1",
            theme: "dark",
            locale: "en",
            toolbar_bg: "#f1f3f6",
            enable_publishing: false,
        });
    }

    // Smooth Scrolling for Navbar
    document.querySelectorAll('.nav-links a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetSection = document.querySelector(this.getAttribute('href'));
            if (targetSection) {
                window.scrollTo({
                    top: targetSection.offsetTop - 80, // Adjust for fixed navbar
                    behavior: 'smooth'
                });
            }
        });
    });
});
