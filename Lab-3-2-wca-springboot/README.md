# Java Code Migration Tool

A command-line tool for migrating Java code between different frameworks and specifications, powered by watsonx Code Assistant (WCA) API.

## Features

- **Specific Migrations**:
  - Struts → Spring Boot
  - EJB → POJO
  - Gradle → Maven

## About

This tool leverages IBM's watsonx Code Assistant (WCA) API to:
- Analyze Java code for modernization opportunities
- Generate migration recommendations
- Transform code between different Java frameworks and specifications
- Preserve business logic while updating implementation patterns
- Convert build configurations between different build systems

## Installation

1. Clone the repository:
```bash
git clone https://github.ibm.com/watsonx-apac/wca-springboot.git
cd wca-springboot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your IBM Cloud API key in `.env` file:
```bash
IAM_APIKEY=your_api_key_here
```

## Usage

### Specific Migrations

#### Struts to Spring Boot

Migrate Struts applications to Spring Boot:

```bash
python wca_springboot.py migrate-structs ./path/to/struts/app
```

The tool intelligently detects Struts applications by looking for multiple indicators:
- struts-config.xml files
- Java files in 'action' directories
- Java files in 'form' directories
- Struts dependencies in pom.xml/build.gradle

At least one of these indicators must be present for migration to proceed. While struts-config.xml is preferred, the tool can attempt migration based on other indicators if it's not found.

By default, the migrated Spring Boot application will be created in `./output/spring-app`. 
You can specify a different output location using the `--output` option:

```bash
python wca_springboot.py migrate-structs ./path/to/struts/app --output ./custom/output/path
```

The migration process includes:

1. **Project Structure**:
   - Creates Spring Boot directory structure
   - Sets up proper package hierarchy
   - Creates necessary resource directories

2. **Controller Migration**:
   - Converts Struts Actions to REST Controllers
   - Adds proper request mappings
   - Implements CRUD operations
   - Adds validation and error handling

3. **DTO Migration**:
   - Converts Form beans to DTOs
   - Adds validation annotations
   - Implements proper getters/setters
   - Removes Struts-specific code

4. **Service Layer Migration**:
   - Converts business logic to Spring Services
   - Adds @Service and @Transactional annotations
   - Implements proper dependency injection
   - Maintains business logic integrity

5. **View Layer Migration**:
   - Converts JSP pages to Thymeleaf templates
   - Handles both list and form templates
   - Adds proper Thymeleaf attributes
   - Implements error handling
   - Maintains responsive design
   - Supports multiple template locations (src/main/resources, target/classes)

6. **Dependency Management**:
   - Creates Maven pom.xml
   - Adds Spring Boot dependencies
   - Configures build process
   - Sets up proper plugin management

#### EJB to POJO

Migrate EJB code to POJOs:

```bash
python wca_springboot.py migrate-ejb-to-pojo path/to/EJBFile.java --output POJOFile.java
```

#### Gradle to Maven

Convert Gradle build files to Maven:

```bash
python wca_springboot.py migrate-gradle-to-maven build.gradle --output pom.xml
```

## Project Structure

The migrated Spring Boot application will have the following structure:

```
output/spring-app/
├── pom.xml
├── src/
    ├── main/
        ├── java/
        │   └── com/example/application/
        │       ├── controller/
        │       ├── model/
        │       ├── service/
        │       └── repository/
        └── resources/
            └── templates/
```

## Code Generation Features

1. **Robust Code Extraction**:
   - Language-specific code block extraction
   - Proper handling of markdown code blocks
   - Maintains code formatting and indentation
   - Removes Watson assistance comments
   - Fallback handling for non-standard responses

2. **Template Handling**:
   - Supports multiple template locations
   - Intelligent template type detection (list/form)
   - Proper path resolution
   - Maintains template hierarchy

3. **Error Handling**:
   - Detailed error messages
   - Path resolution fallbacks
   - Exception tracking
   - Progress reporting

## Testing

Run the test suite:

```bash
pytest tests -vx
```

Tests cover:
- Spring structure creation
- Controller conversion
- DTO migration
- Service layer migration
- Template conversion
- Dependency management

## Requirements

- Python 3.8+
- IBM Cloud API key
- Java source files to analyze/migrate

## Dependencies

- typer: CLI interface
- rich: Terminal formatting
- python-dotenv: Environment variable management
- requests: API communication