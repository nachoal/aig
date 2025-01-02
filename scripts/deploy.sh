#!/bin/bash

# Exit on error
set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting deployment process...${NC}"

# Clean any existing build artifacts
echo -e "${GREEN}Cleaning old build artifacts...${NC}"
rm -rf dist/ build/ *.egg-info/

# Build the package
echo -e "${GREEN}Building package with uv...${NC}"
uv build

# Upload to PyPI
echo -e "${GREEN}Uploading to PyPI...${NC}"
if uvx twine upload dist/*; then
    echo -e "${GREEN}Upload successful!${NC}"
    
    # Clean up build artifacts
    echo -e "${GREEN}Cleaning up build artifacts...${NC}"
    rm -rf dist/ build/ *.egg-info/
    
    echo -e "${GREEN}Deployment completed successfully!${NC}"
else
    echo -e "${RED}Upload failed! Keeping build artifacts for inspection.${NC}"
    exit 1
fi 