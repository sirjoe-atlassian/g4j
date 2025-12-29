#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { program } = require('commander');
const Mustache = require('mustache');

// Template for unit tests
const UNIT_TEST_TEMPLATE = `/**
 * Unit tests for {{moduleName}}
 * Generated on: {{timestamp}}
 */

describe('{{moduleName}}', () => {
  {{#testCases}}
  test('{{description}}', () => {
    // Arrange
    {{#arrange}}
    {{{.}}}
    {{/arrange}}
    
    // Act
    {{#act}}
    {{{.}}}
    {{/act}}
    
    // Assert
    {{#assert}}
    {{{.}}}
    {{/assert}}
  });

  {{/testCases}}
});
`;

// Template for integration tests
const INTEGRATION_TEST_TEMPLATE = `/**
 * Integration tests for {{moduleName}}
 * Generated on: {{timestamp}}
 */

describe('{{moduleName}} Integration Tests', () => {
  beforeAll(async () => {
    // Setup integration test environment
    {{#setup}}
    {{{.}}}
    {{/setup}}
  });

  afterAll(async () => {
    // Cleanup integration test environment
    {{#cleanup}}
    {{{.}}}
    {{/cleanup}}
  });

  {{#testCases}}
  test('{{description}}', async () => {
    // Arrange
    {{#arrange}}
    {{{.}}}
    {{/arrange}}
    
    // Act
    {{#act}}
    {{{.}}}
    {{/act}}
    
    // Assert
    {{#assert}}
    {{{.}}}
    {{/assert}}
  });

  {{/testCases}}
});
`;

// Template for E2E tests
const E2E_TEST_TEMPLATE = `/**
 * End-to-End tests for {{featureName}}
 * Generated on: {{timestamp}}
 */

describe('{{featureName}} E2E Tests', () => {
  beforeAll(async () => {
    // Initialize E2E test environment
    {{#setup}}
    {{{.}}}
    {{/setup}}
  });

  afterAll(async () => {
    // Cleanup E2E test environment
    {{#cleanup}}
    {{{.}}}
    {{/cleanup}}
  });

  {{#scenarios}}
  test('{{scenario}}', async () => {
    // Given
    {{#given}}
    {{{.}}}
    {{/given}}
    
    // When
    {{#when}}
    {{{.}}}
    {{/when}}
    
    // Then
    {{#then}}
    {{{.}}}
    {{/then}}
  });

  {{/scenarios}}
});
`;

class TestGenerator {
  constructor() {
    this.templates = {
      unit: UNIT_TEST_TEMPLATE,
      integration: INTEGRATION_TEST_TEMPLATE,
      e2e: E2E_TEST_TEMPLATE
    };
  }

  generateTest(type, config) {
    const template = this.templates[type];
    if (!template) {
      throw new Error(`Unknown test type: ${type}`);
    }

    const data = {
      ...config,
      timestamp: new Date().toISOString()
    };

    return Mustache.render(template, data);
  }

  writeTestFile(type, filename, config) {
    const testDir = path.join('tests', type);
    
    // Ensure directory exists
    if (!fs.existsSync(testDir)) {
      fs.mkdirSync(testDir, { recursive: true });
    }

    const testContent = this.generateTest(type, config);
    const filePath = path.join(testDir, filename);
    
    fs.writeFileSync(filePath, testContent);
    console.log(`✓ Generated ${type} test: ${filePath}`);
    
    return filePath;
  }

  generateFromConfig(configPath) {
    const configContent = fs.readFileSync(configPath, 'utf8');
    const config = JSON.parse(configContent);

    const results = [];
    
    if (config.tests) {
      config.tests.forEach(testConfig => {
        const { type, filename, ...testData } = testConfig;
        const filePath = this.writeTestFile(type, filename, testData);
        results.push(filePath);
      });
    }

    return results;
  }
}

// CLI configuration
program
  .name('test-generator')
  .description('Generate test automation code')
  .version('1.0.0');

program
  .command('generate')
  .description('Generate test files from configuration')
  .option('-c, --config <path>', 'Path to configuration file')
  .option('-t, --type <type>', 'Test type (unit|integration|e2e)')
  .option('-n, --name <name>', 'Module/Feature name')
  .option('-o, --output <filename>', 'Output filename')
  .action((options) => {
    const generator = new TestGenerator();

    if (options.config) {
      // Generate from config file
      console.log(`Generating tests from config: ${options.config}`);
      const results = generator.generateFromConfig(options.config);
      console.log(`\n✓ Generated ${results.length} test file(s)`);
    } else if (options.type && options.name && options.output) {
      // Generate single test file
      const config = {
        moduleName: options.name,
        featureName: options.name,
        testCases: [
          {
            description: 'should work correctly',
            arrange: ['// TODO: Setup test data'],
            act: ['// TODO: Execute function/method'],
            assert: ['// TODO: Verify expected results']
          }
        ],
        scenarios: [
          {
            scenario: 'should work end-to-end',
            given: ['// TODO: Initial state'],
            when: ['// TODO: User action'],
            then: ['// TODO: Expected outcome']
          }
        ],
        setup: ['// TODO: Setup code'],
        cleanup: ['// TODO: Cleanup code']
      };

      generator.writeTestFile(options.type, options.output, config);
    } else {
      console.error('Error: Please provide either --config or all of --type, --name, and --output');
      process.exit(1);
    }
  });

program
  .command('init')
  .description('Initialize test automation configuration')
  .option('-o, --output <path>', 'Output path for config file', 'test-config.json')
  .action((options) => {
    const exampleConfig = {
      tests: [
        {
          type: 'unit',
          filename: 'example.test.js',
          moduleName: 'ExampleModule',
          testCases: [
            {
              description: 'should return correct value',
              arrange: ['const input = "test";'],
              act: ['const result = exampleFunction(input);'],
              assert: ['expect(result).toBe("expected");']
            }
          ]
        }
      ]
    };

    fs.writeFileSync(options.output, JSON.stringify(exampleConfig, null, 2));
    console.log(`✓ Created example configuration: ${options.output}`);
  });

// If running as script
if (require.main === module) {
  program.parse(process.argv);
}

module.exports = { TestGenerator };
