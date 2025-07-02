"""
System Monitor Root Agent

This module defines the root agent for the system monitoring application.
It uses a parallel agent for system information gathering and a sequential
pipeline for the overall flow.
"""
from config.logger_config import log

try:
    from google.adk.agents import ParallelAgent, SequentialAgent
    from .subagents.cpu_info_agent import cpu_info_agent
    from .subagents.disk_info_agent import disk_info_agent
    from .subagents.memory_info_agent import memory_info_agent
    from .subagents.synthesizer_agent import system_report_synthesizer

    log.info("Successfully imported all necessary modules and agents.")

    system_info_gatherer = ParallelAgent(
        name="system_info_gatherer",
        sub_agents=[cpu_info_agent, memory_info_agent, disk_info_agent],
    )
    log.info("System info gatherer parallel agent created successfully.")

    root_agent = SequentialAgent(
        name="system_monitor_agent",
        sub_agents=[system_info_gatherer, system_report_synthesizer],
    )
    log.info("System monitor root sequential agent created successfully.")

except ImportError as e:
    log.error(f"Error importing a module: {e}")
except Exception as e:
    log.error(f"An unexpected error occurred: {e}")