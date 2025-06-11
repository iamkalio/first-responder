/*instrumentation.js*/
const {
    getNodeAutoInstrumentations,
} = require('@opentelemetry/auto-instrumentations-node');
const {
    OTLPTraceExporter,
} = require('@opentelemetry/exporter-trace-otlp-proto');
const {
    OTLPMetricExporter,
} = require('@opentelemetry/exporter-metrics-otlp-proto');
const { NodeSDK } = require('@opentelemetry/sdk-node');
const {
    PeriodicExportingMetricReader,
} = require('@opentelemetry/sdk-metrics');
const { resourceFromAttributes } = require('@opentelemetry/resources');
const {
    ATTR_SERVICE_NAME,
    ATTR_SERVICE_VERSION,
} = require('@opentelemetry/semantic-conventions');


// Get the OTLP endpoint from environment variable, with a fallback
const otlpEndpoint = process.env.OTEL_EXPORTER_OTLP_ENDPOINT || 'http://localhost:4318';

// Log the endpoint being used - CRUCIAL FOR DEBUGGING
console.log(`OpenTelemetry will export to OTLP endpoint: ${otlpEndpoint}`);

const sdk = new NodeSDK({
    resource: resourceFromAttributes({
        [ATTR_SERVICE_NAME]: 'dice-server',
        [ATTR_SERVICE_VERSION]: '0.1.0',
    }),
    traceExporter: new OTLPTraceExporter({
        url: `${otlpEndpoint}/v1/traces`, 
    }),
    metricReader: new PeriodicExportingMetricReader({
        exporter: new OTLPMetricExporter({
            url: `${otlpEndpoint}/v1/metrics`,
        }),
        exportIntervalMillis: 5000,
    }),
    instrumentations: [getNodeAutoInstrumentations()],
});

sdk.start();

console.log('OpenTelemetry SDK started successfully. Check application logs for OTLP export activity.');