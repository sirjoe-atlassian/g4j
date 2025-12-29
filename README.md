# g4j - Test Automation Framework

A comprehensive test automation framework with code generation capabilities for Node.js projects.

## Features

- **Automated Test Generation**: Generate unit, integration, and E2E tests from templates or configuration files
- **CLI Tool**: Easy-to-use command-line interface for quick test scaffolding
- **Multiple Test Types**: Support for unit tests, integration tests, and end-to-end tests
- **Configuration-Based**: Generate multiple test files from a single JSON configuration
- **Jest Integration**: Built-in support for Jest testing framework

## Quick Start

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Generate tests from configuration:**
   ```bash
   node src/test-automation/generator.js generate --config test-config.example.json
   ```

3. **Generate a single test file:**
   ```bash
   node src/test-automation/generator.js generate --type unit --name MyModule --output my-module.test.js
   ```

4. **Run tests:**
   ```bash
   npm test
   ```

## Documentation

For detailed documentation on the test automation framework, see [README-TEST-AUTOMATION.md](README-TEST-AUTOMATION.md)

## Project Structure

```
.
├── src/
│   └── test-automation/     # Test generation framework
│       ├── generator.js      # CLI and generation logic
│       └── index.js          # Main entry point
├── tests/
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── e2e/                  # End-to-end tests
├── package.json
├── jest.config.js
├── test-config.example.json  # Example configuration
└── README-TEST-AUTOMATION.md # Detailed documentation
```

## Usage Examples

### Initialize Configuration
```bash
node src/test-automation/generator.js init
```

### Generate Unit Test
```bash
node src/test-automation/generator.js generate \
  --type unit \
  --name Calculator \
  --output calculator.test.js
```

### Run Specific Test Types
```bash
npm run test:unit          # Run unit tests
npm run test:integration   # Run integration tests
npm run test:e2e          # Run E2E tests
npm run test:coverage     # Generate coverage report
```

## License

MIT - See [licence.md](licence.md) for details