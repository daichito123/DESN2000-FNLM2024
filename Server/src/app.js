// const ctx = document.getElementById('scatterChart').getContext('2d');
const scatterData = {
    datasets: [{
        label: 'Scatter Dataset',
        data: [
            { x: -10, y: 0 },
            { x: 0, y: 10 },
            { x: 10, y: 5 },
            { x: 0.5, y: 5.5 }
        ],
        backgroundColor: 'rgba(75, 192, 192, 1)'
    }]
};

const scatterChart = new Chart("scatterChart", {
    type: 'scatter',
    data: scatterData,
    options: {
        scales: {
            x: {
                type: 'linear', 
                position: 'bottom'
            }
        }
    }
});
