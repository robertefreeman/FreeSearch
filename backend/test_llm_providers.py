#!/usr/bin/env python3
"""
Test script to demonstrate OpenAI-compatible LLM provider support.

This script shows how to configure the agent to use different LLM providers:
- Gemini (default)
- OpenAI-compatible providers

Usage:
    # Test with Gemini (default)
    GEMINI_API_KEY=your_key python test_llm_providers.py

    # Test with OpenAI
    LLM_PROVIDER=openai OPENAI_API_KEY=your_key python test_llm_providers.py

    # Test with OpenAI-compatible provider (e.g., Ollama, Together, etc.)
    LLM_PROVIDER=openai OPENAI_API_KEY=your_key OPENAI_API_BASE=http://localhost:11434/v1 python test_llm_providers.py
"""

import os
import sys

# Set dummy API keys before importing to avoid validation errors
if not os.getenv("GEMINI_API_KEY") and not os.getenv("OPENAI_API_KEY"):
    os.environ["GEMINI_API_KEY"] = "dummy-key"

sys.path.insert(0, 'src')

from agent.configuration import Configuration
from agent.graph import create_llm

def test_gemini_provider():
    """Test Gemini provider configuration."""
    print("=== Testing Gemini Provider ===")
    
    config = Configuration(llm_provider="gemini")
    print(f"Provider: {config.llm_provider}")
    print(f"Query model: {config.query_generator_model}")
    print(f"Reflection model: {config.reflection_model}")
    print(f"Answer model: {config.answer_model}")
    
    try:
        llm = create_llm(config.query_generator_model, 1.0, 2, config)
        print(f"✓ Successfully created {type(llm).__name__}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def test_openai_provider():
    """Test OpenAI provider configuration."""
    print("\n=== Testing OpenAI Provider ===")
    
    config = Configuration(
        llm_provider="openai",
        query_generator_model="gpt-4o-mini",
        reflection_model="gpt-4o",
        answer_model="gpt-4o",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    )
    
    print(f"Provider: {config.llm_provider}")
    print(f"API Base: {config.openai_api_base}")
    print(f"Query model: {config.query_generator_model}")
    print(f"Reflection model: {config.reflection_model}")
    print(f"Answer model: {config.answer_model}")
    
    try:
        llm = create_llm(config.query_generator_model, 1.0, 2, config)
        print(f"✓ Successfully created {type(llm).__name__}")
        print(f"  Model: {llm.model_name}")
        print(f"  Base URL: {getattr(llm, 'openai_api_base', 'Not set')}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def main():
    """Main test function."""
    print("LLM Provider Support Test")
    print("=" * 50)
    
    provider = os.getenv("LLM_PROVIDER", "gemini").lower()
    
    if provider == "gemini":
        if not os.getenv("GEMINI_API_KEY"):
            print("⚠️  GEMINI_API_KEY not set, using dummy key for testing")
            os.environ["GEMINI_API_KEY"] = "dummy-key"
        
        success = test_gemini_provider()
        
    elif provider == "openai":
        if not os.getenv("OPENAI_API_KEY"):
            print("⚠️  OPENAI_API_KEY not set, using dummy key for testing")
            os.environ["OPENAI_API_KEY"] = "dummy-key"
        
        success = test_openai_provider()
        
    else:
        print(f"✗ Unknown provider: {provider}")
        print("Supported providers: gemini, openai")
        success = False
    
    print("\n" + "=" * 50)
    if success:
        print("✓ Test completed successfully!")
        print("\nTo use this in production:")
        if provider == "gemini":
            print("1. Set GEMINI_API_KEY environment variable")
            print("2. Optionally configure model names via environment variables")
        else:
            print("1. Set LLM_PROVIDER=openai")
            print("2. Set OPENAI_API_KEY environment variable") 
            print("3. Optionally set OPENAI_API_BASE for custom endpoints")
            print("4. Optionally configure model names via environment variables")
    else:
        print("✗ Test failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()