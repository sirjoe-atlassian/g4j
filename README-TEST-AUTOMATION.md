# Test Automation Framework

This test automation framework provides code generation capabilities to quickly scaffold test files for unit, integration, and end-to-end testing.

## Features

- **Test Code Generation**: Automatically generate test files from templates
- **Multiple Test Types**: Support for unit, integration, and E2E tests
- **Configuration-Based**: Generate multiple tests from a single config file
- **CLI Tool**: Easy-to-use command-line interface
- **Template-Based**: Uses Mustache templates for flexible test generation

## Installation

```bash
npm install
```

## Usage

### Initialize Configuration

Create an example configuration file:

```bash
npm run generate:test -- init
```

This creates a `test-config.json` file with example test configurations.

### Generate Tests from Configuration

```bash
node src/test-automation/generator.js generate --config test-config.example.json
```

### Generate Single Test File

Generate a unit test:
```bash
node src/test-automation/generator.js generate --type unit --name MyModule --output my-module.test.js
```

Generate an integration test:
```bash
node src/test-automation/generator.js generate --type integration --name UserService --output user-service.test.js
```

Generate an E2E test:
```bash
node src/test-automation/generator.js generate --type e2e --name "Login Feature" --output login.test.js
```

## Running Tests

Run all tests:
```bash
npm test
```

Run specific test types:
```bash
npm run test:unit          # Run unit tests only
npm run test:integration   # Run integration tests only
npm run test:e2e          # Run E2E tests only
```

Run tests in watch mode:
```bash
npm run test:watch
```

Generate coverage report:
```bash
npm run test:coverage
```

## Test Configuration Format

Create a `test-config.json` file with the following structure:

### Unit Test Configuration

```json
{
  "tests": [
    {
      "type": "unit",
      "filename": "example.test.js",
      "moduleName": "ExampleModule",
      "testCases": [
        {
          "description": "should do something",
          "arrange": ["const input = 'test';"],
          "act": ["const result = exampleFunction(input);"],
          "assert": ["expect(result).toBe('expected');"]
        }
      ]
    }
  ]
}
```

### Integration Test Configuration

```json
{
  "type": "integration",
  "filename": "service.test.js",
  "moduleName": "MyService",
  "setup": ["await database.connect();"],
  "cleanup": ["await database.disconnect();"],
  "testCases": [
    {
      "description": "should integrate correctly",
      "arrange": ["const data = { id: 1 };"],
      "act": ["const result = await service.process(data);"],
      "assert": ["expect(result).toBeDefined();"]
    }
  ]
}
```

### E2E Test Configuration

```json
{
  "type": "e2e",
  "filename": "feature.test.js",
  "featureName": "My Feature",
  "setup": ["await browser.launch();"],
  "cleanup": ["await browser.close();"],
  "scenarios": [
    {
      "scenario": "user can complete workflow",
      "given": ["await page.goto('/');"],
      "when": ["await page.click('#submit');"],
      "then": ["await expect(page).toHaveURL('/success');"]
    }
  ]
}
```

## Directory Structure

```
.
├── src/
│   └── test-automation/
│       ├── generator.js      # Test generator CLI and logic
│       └── index.js          # Main entry point
├── tests/
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── e2e/                  # End-to-end tests
├── package.json
├── jest.config.js
└── test-config.example.json  # Example configuration
```

## CLI Commands

```bash
# Initialize configuration
node src/test-automation/generator.js init [--output <path>]

# Generate tests
node src/test-automation/generator.js generate --config <config-file>
node src/test-automation/generator.js generate --type <type> --name <name> --output <filename>

# Get help
node src/test-automation/generator.js --help
node src/test-automation/generator.js generate --help
```

## Examples

See `test-config.example.json` for complete examples of:
- Calculator unit tests
- User service integration tests
- Login flow E2E tests

## Extending the Framework

You can customize the test templates in `src/test-automation/generator.js` by modifying:
- `UNIT_TEST_TEMPLATE`
- `INTEGRATION_TEST_TEMPLATE`
- `E2E_TEST_TEMPLATE`

## License

MIT - See licence.md for details
