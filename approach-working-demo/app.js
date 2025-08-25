// AI Approaches Demo - Top-Down vs Bottom-Up
class AIApproachesDemo {
    constructor() {
        this.selectedShape = null;
        this.isAnalyzing = false;
        this.analysisResults = {
            topDown: null,
            bottomUp: null
        };
        
        // Shape data from the provided JSON
        this.shapes = {
            circle: {
                name: "circle",
                display: "Circle", 
                rules: {
                    corners: 0,
                    curves: 1,
                    symmetry: "radial",
                    equal_sides: false
                },
                features: [0.1, 0.9, 0.2, 0.1, 0.8, 0.9, 0.1, 0.2],
                icon: "○"
            },
            square: {
                name: "square",
                display: "Square",
                rules: {
                    corners: 4,
                    curves: 0,
                    symmetry: "4-fold",
                    equal_sides: true
                },
                features: [0.9, 0.1, 0.9, 0.9, 0.2, 0.1, 0.9, 0.8],
                icon: "□"
            },
            triangle: {
                name: "triangle", 
                display: "Triangle",
                rules: {
                    corners: 3,
                    curves: 0,
                    symmetry: "3-fold",
                    equal_sides: true
                },
                features: [0.7, 0.2, 0.7, 0.6, 0.3, 0.2, 0.7, 0.5],
                icon: "△"
            },
            rectangle: {
                name: "rectangle",
                display: "Rectangle", 
                rules: {
                    corners: 4,
                    curves: 0,
                    symmetry: "2-fold",
                    equal_sides: false
                },
                features: [0.8, 0.1, 0.8, 0.6, 0.2, 0.1, 0.8, 0.4],
                icon: "▭"
            }
        };

        this.ruleTemplates = {
            circle: [
                "Has 0 corners",
                "Has curved edges", 
                "Radial symmetry",
                "No straight sides"
            ],
            square: [
                "Has 4 corners",
                "All sides equal",
                "All angles 90°",
                "4-fold symmetry"
            ],
            triangle: [
                "Has 3 corners",
                "3 straight sides",
                "Angles sum to 180°",
                "3-fold symmetry"
            ],
            rectangle: [
                "Has 4 corners", 
                "Opposite sides equal",
                "All angles 90°",
                "2-fold symmetry"
            ]
        };

        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.init());
        } else {
            this.init();
        }
    }

    init() {
        console.log('Initializing AI Approaches Demo');
        this.setupEventHandlers();
        this.drawInitialCanvas();
        this.hideAnalysisResults();
    }

    setupEventHandlers() {
        console.log('Setting up event handlers');
        
        // Shape selection buttons
        const shapeButtons = document.querySelectorAll('.shape-btn');
        console.log('Found shape buttons:', shapeButtons.length);
        
        shapeButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const shape = btn.getAttribute('data-shape');
                console.log('Shape button clicked:', shape);
                this.selectShape(shape);
            });
        });

        // Analyze button
        const analyzeBtn = document.getElementById('analyze-btn');
        if (analyzeBtn) {
            console.log('Setting up analyze button');
            analyzeBtn.addEventListener('click', (e) => {
                e.preventDefault();
                console.log('Analyze button clicked');
                this.analyzeShape();
            });
        }

        // Reset demo button
        const resetBtn = document.getElementById('reset-demo');
        if (resetBtn) {
            console.log('Setting up reset button');
            resetBtn.addEventListener('click', (e) => {
                e.preventDefault();
                console.log('Reset button clicked');
                this.resetDemo();
            });
        }

        // Compare all button
        const compareBtn = document.getElementById('compare-all');
        if (compareBtn) {
            console.log('Setting up compare all button');
            compareBtn.addEventListener('click', (e) => {
                e.preventDefault();
                this.compareAllShapes();
            });
        }
    }

    selectShape(shapeName) {
        if (this.isAnalyzing) return;

        console.log('Selecting shape:', shapeName);

        // Update button states
        document.querySelectorAll('.shape-btn').forEach(btn => {
            btn.classList.remove('selected');
        });

        const selectedBtn = document.querySelector(`[data-shape="${shapeName}"]`);
        if (selectedBtn) {
            selectedBtn.classList.add('selected');
            console.log('Shape button selected');
        }

        this.selectedShape = shapeName;
        this.drawShape(shapeName);
        
        // Enable analyze button
        const analyzeBtn = document.getElementById('analyze-btn');
        if (analyzeBtn) {
            analyzeBtn.disabled = false;
            console.log('Analyze button enabled');
        }

        // Hide previous results
        this.hideAnalysisResults();
    }

    drawInitialCanvas() {
        const canvas = document.getElementById('shape-canvas');
        if (!canvas) {
            console.log('Canvas not found');
            return;
        }

        console.log('Drawing initial canvas');
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw placeholder
        ctx.strokeStyle = '#ccc';
        ctx.setLineDash([5, 5]);
        ctx.strokeRect(20, 20, 160, 160);
        ctx.setLineDash([]);

        ctx.fillStyle = '#999';
        ctx.font = '16px Arial, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('Select a shape', canvas.width / 2, canvas.height / 2);
    }

    drawShape(shapeName) {
        const canvas = document.getElementById('shape-canvas');
        if (!canvas) {
            console.log('Canvas not found for drawing shape');
            return;
        }

        console.log('Drawing shape:', shapeName);
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Set style
        ctx.strokeStyle = '#218087';
        ctx.fillStyle = 'rgba(33, 128, 135, 0.2)';
        ctx.lineWidth = 3;

        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;

        switch (shapeName) {
            case 'circle':
                ctx.beginPath();
                ctx.arc(centerX, centerY, 60, 0, 2 * Math.PI);
                ctx.fill();
                ctx.stroke();
                break;

            case 'square':
                const size = 100;
                const x = centerX - size / 2;
                const y = centerY - size / 2;
                ctx.fillRect(x, y, size, size);
                ctx.strokeRect(x, y, size, size);
                break;

            case 'triangle':
                ctx.beginPath();
                ctx.moveTo(centerX, centerY - 60);
                ctx.lineTo(centerX - 60, centerY + 40);
                ctx.lineTo(centerX + 60, centerY + 40);
                ctx.closePath();
                ctx.fill();
                ctx.stroke();
                break;

            case 'rectangle':
                const width = 120;
                const height = 70;
                const rectX = centerX - width / 2;
                const rectY = centerY - height / 2;
                ctx.fillRect(rectX, rectY, width, height);
                ctx.strokeRect(rectX, rectY, width, height);
                break;
        }
    }

    hideAnalysisResults() {
        const analysisResults = document.getElementById('analysis-results');
        const resultsComparison = document.getElementById('results-comparison');
        
        if (analysisResults) {
            analysisResults.style.opacity = '0.3';
        }
        if (resultsComparison) {
            resultsComparison.classList.remove('active');
        }
    }

    showAnalysisResults() {
        const analysisResults = document.getElementById('analysis-results');
        const resultsComparison = document.getElementById('results-comparison');
        
        if (analysisResults) {
            analysisResults.style.opacity = '1';
        }
        if (resultsComparison) {
            setTimeout(() => {
                resultsComparison.classList.add('active');
            }, 2000);
        }
    }

    async analyzeShape() {
        if (!this.selectedShape || this.isAnalyzing) {
            console.log('Cannot analyze - no shape selected or already analyzing');
            return;
        }

        console.log('Starting analysis for shape:', this.selectedShape);
        this.isAnalyzing = true;
        
        // Update analyze button
        const analyzeBtn = document.getElementById('analyze-btn');
        if (analyzeBtn) {
            analyzeBtn.disabled = true;
            analyzeBtn.textContent = 'Analyzing...';
        }

        // Show analysis results
        this.showAnalysisResults();

        // Run both analyses simultaneously
        try {
            await Promise.all([
                this.runTopDownAnalysis(),
                this.runBottomUpAnalysis()
            ]);

            // Show final results
            this.displayComparisonResults();

            if (analyzeBtn) {
                analyzeBtn.textContent = 'Analysis Complete';
            }
        } catch (error) {
            console.error('Error during analysis:', error);
        }

        this.isAnalyzing = false;
    }

    async runTopDownAnalysis() {
        console.log('Running top-down analysis');
        const shape = this.shapes[this.selectedShape];
        const ruleSteps = document.getElementById('rule-steps');
        const processing = document.getElementById('topdown-processing');
        const confidenceFill = document.getElementById('topdown-confidence');
        const confidenceText = document.getElementById('topdown-percentage');

        // Show processing indicator
        if (processing) {
            processing.classList.add('active');
        }

        // Clear previous results
        if (ruleSteps) {
            ruleSteps.innerHTML = '';
        }

        await this.delay(800);

        // Hide processing indicator
        if (processing) {
            processing.classList.remove('active');
        }

        const rules = this.ruleTemplates[this.selectedShape];
        let passedRules = 0;

        // Evaluate each rule step by step
        for (let i = 0; i < rules.length; i++) {
            const rule = rules[i];
            const stepElement = document.createElement('div');
            stepElement.className = 'rule-step checking';
            stepElement.textContent = `Checking: ${rule}...`;

            if (ruleSteps) {
                ruleSteps.appendChild(stepElement);
                // Force reflow to ensure the element is added
                stepElement.offsetHeight;
                stepElement.classList.add('show');
            }

            await this.delay(1000);

            // All rules pass for the correct shape (simplified logic)
            const passes = true;
            if (passes) {
                stepElement.className = 'rule-step passed show';
                stepElement.textContent = `✓ ${rule}`;
                passedRules++;
            } else {
                stepElement.className = 'rule-step failed show';
                stepElement.textContent = `✗ ${rule}`;
            }

            await this.delay(400);
        }

        const confidence = Math.round((passedRules / rules.length) * 100);

        // Update confidence meter
        if (confidenceFill) {
            setTimeout(() => {
                confidenceFill.style.width = `${confidence}%`;
            }, 300);
        }
        if (confidenceText) {
            setTimeout(() => {
                confidenceText.textContent = `${confidence}%`;
            }, 300);
        }

        this.analysisResults.topDown = {
            shape: shape.display,
            confidence: confidence,
            reasoning: `Rule-based classification: ${passedRules}/${rules.length} rules matched`
        };
    }

    async runBottomUpAnalysis() {
        console.log('Running bottom-up analysis');
        const shape = this.shapes[this.selectedShape];
        const processing = document.getElementById('bottomup-processing');
        const networkViz = document.getElementById('network-viz');
        const confidenceFill = document.getElementById('bottomup-confidence');
        const confidenceText = document.getElementById('bottomup-percentage');

        // Show processing indicator
        if (processing) {
            processing.classList.add('active');
        }

        await this.delay(600);

        // Create neural network visualization
        this.createNeuralNetwork();

        await this.delay(800);

        // Hide processing, show network
        if (processing) {
            processing.classList.remove('active');
        }
        if (networkViz) {
            networkViz.classList.add('active');
        }

        // Simulate network processing
        await this.simulateNetworkProcessing(shape.features);

        // Calculate confidence (simulate realistic but high confidence)
        const confidence = Math.round(85 + Math.random() * 12);

        // Update confidence meter
        if (confidenceFill) {
            confidenceFill.style.width = `${confidence}%`;
        }
        if (confidenceText) {
            confidenceText.textContent = `${confidence}%`;
        }

        this.analysisResults.bottomUp = {
            shape: shape.display,
            confidence: confidence,
            reasoning: `Neural network classification based on 8 learned features`
        };
    }

    createNeuralNetwork() {
        console.log('Creating neural network visualization');
        const inputNodes = document.getElementById('input-nodes');
        const hiddenNodes = document.getElementById('hidden-nodes');
        const outputNodes = document.getElementById('output-nodes');

        // Create input nodes
        if (inputNodes) {
            inputNodes.innerHTML = '';
            for (let i = 0; i < 8; i++) {
                const node = document.createElement('div');
                node.className = 'node';
                node.id = `input-${i}`;
                inputNodes.appendChild(node);
            }
        }

        // Create hidden nodes
        if (hiddenNodes) {
            hiddenNodes.innerHTML = '';
            for (let i = 0; i < 6; i++) {
                const node = document.createElement('div');
                node.className = 'node';
                node.id = `hidden-${i}`;
                hiddenNodes.appendChild(node);
            }
        }

        // Create output nodes
        if (outputNodes) {
            outputNodes.innerHTML = '';
            const outputs = ['Circle', 'Square', 'Triangle', 'Rectangle'];
            for (let i = 0; i < 4; i++) {
                const node = document.createElement('div');
                node.className = 'node';
                node.id = `output-${i}`;
                node.title = outputs[i];
                outputNodes.appendChild(node);
            }
        }
    }

    async simulateNetworkProcessing(features) {
        console.log('Simulating network processing');
        // Reset all nodes
        document.querySelectorAll('.node').forEach(node => {
            node.classList.remove('active', 'processing');
        });

        await this.delay(300);

        // Activate input nodes based on features
        for (let i = 0; i < Math.min(8, features.length); i++) {
            const node = document.getElementById(`input-${i}`);
            if (node && features[i] > 0.4) {
                node.classList.add('active');
            }
            await this.delay(150);
        }

        await this.delay(600);

        // Process hidden layer
        for (let i = 0; i < 6; i++) {
            const node = document.getElementById(`hidden-${i}`);
            if (node) {
                node.classList.add('processing');
                await this.delay(200);
                
                // Most hidden nodes activate
                if (Math.random() > 0.15) {
                    node.classList.remove('processing');
                    node.classList.add('active');
                }
            }
        }

        await this.delay(700);

        // Activate correct output
        const shapeIndex = Object.keys(this.shapes).indexOf(this.selectedShape);
        for (let i = 0; i < 4; i++) {
            const node = document.getElementById(`output-${i}`);
            if (node) {
                if (i === shapeIndex) {
                    node.classList.add('active');
                }
                await this.delay(180);
            }
        }
    }

    displayComparisonResults() {
        console.log('Displaying comparison results');
        const tdShape = document.getElementById('td-shape');
        const tdConf = document.getElementById('td-conf');
        const tdReason = document.getElementById('td-reason');
        const buShape = document.getElementById('bu-shape');
        const buConf = document.getElementById('bu-conf');
        const buReason = document.getElementById('bu-reason');

        if (!this.analysisResults.topDown || !this.analysisResults.bottomUp) {
            console.log('Analysis results not ready');
            return;
        }

        if (tdShape) tdShape.textContent = this.analysisResults.topDown.shape;
        if (tdConf) tdConf.textContent = `${this.analysisResults.topDown.confidence}%`;
        if (tdReason) tdReason.textContent = this.analysisResults.topDown.reasoning;

        if (buShape) buShape.textContent = this.analysisResults.bottomUp.shape;
        if (buConf) buConf.textContent = `${this.analysisResults.bottomUp.confidence}%`;
        if (buReason) buReason.textContent = this.analysisResults.bottomUp.reasoning;
    }

    resetDemo() {
        if (this.isAnalyzing) return;

        console.log('Resetting demo');
        this.selectedShape = null;
        this.analysisResults = { topDown: null, bottomUp: null };

        // Reset shape selection
        document.querySelectorAll('.shape-btn').forEach(btn => {
            btn.classList.remove('selected');
        });

        // Reset canvas
        this.drawInitialCanvas();

        // Reset analyze button
        const analyzeBtn = document.getElementById('analyze-btn');
        if (analyzeBtn) {
            analyzeBtn.disabled = true;
            analyzeBtn.textContent = 'Analyze Shape';
        }

        // Hide results
        this.hideAnalysisResults();

        // Clear analysis sections
        const ruleSteps = document.getElementById('rule-steps');
        if (ruleSteps) {
            ruleSteps.innerHTML = '';
        }

        // Reset confidence meters
        const confidenceFills = document.querySelectorAll('.meter-fill');
        confidenceFills.forEach(fill => {
            fill.style.width = '0%';
        });

        const confidenceTexts = document.querySelectorAll('.confidence-text');
        confidenceTexts.forEach(text => {
            text.textContent = '0%';
        });

        // Reset neural network
        document.querySelectorAll('.node').forEach(node => {
            node.classList.remove('active', 'processing');
        });

        // Reset processing indicators
        document.querySelectorAll('.processing-indicator').forEach(indicator => {
            indicator.classList.remove('active');
        });

        // Reset network visualization
        const networkViz = document.getElementById('network-viz');
        if (networkViz) {
            networkViz.classList.remove('active');
        }

        // Clear result displays
        const resultElements = ['td-shape', 'td-conf', 'td-reason', 'bu-shape', 'bu-conf', 'bu-reason'];
        resultElements.forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                if (id.includes('shape')) {
                    element.textContent = '-';
                } else if (id.includes('conf')) {
                    element.textContent = '0%';
                } else {
                    element.textContent = 'No analysis yet';
                }
            }
        });
    }

    async compareAllShapes() {
        if (this.isAnalyzing) return;

        alert('Compare All Shapes feature would cycle through each shape and show results side by side. This demonstrates how both approaches perform across different inputs.');
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Initialize the demo
let demoInstance = null;

function initDemo() {
    if (!demoInstance) {
        demoInstance = new AIApproachesDemo();
    }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initDemo);
} else {
    initDemo();
}