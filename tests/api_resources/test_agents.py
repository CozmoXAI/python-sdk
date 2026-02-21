# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cozmoai import Cozmoai, AsyncCozmoai
from tests.utils import assert_matches_type
from cozmoai.types import (
    AgentResponse,
    AgentListResponse,
    AgentDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Cozmoai) -> None:
        agent = client.agents.create(
            org_id="org_id",
            name="name",
            prompt_template="prompt_template",
            type="voice",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Cozmoai) -> None:
        agent = client.agents.create(
            org_id="org_id",
            name="name",
            prompt_template="prompt_template",
            type="voice",
            allowed_sip_trunks=["string"],
            background_sound={
                "file": "file",
                "enabled": True,
                "initial_volume": 0,
                "thinking_sound": [
                    {
                        "sound": "sound",
                        "probability": 0,
                        "volume": 0,
                    }
                ],
                "volume": 0,
            },
            extra_config={
                "allow_interruptions": True,
                "interruption_sensitivity": 0,
                "min_words": 0,
                "turn_detector_enabled": True,
                "turn_detector_is_multilingual": True,
                "turn_detector_model_type": "turn_detector_model_type",
            },
            goodbye_config={
                "enabled": True,
                "message": "message",
            },
            greeting_config={
                "agent_speaks_first": True,
                "greeting": "greeting",
                "pause_before_first_message": 0,
                "voice_mail_message": "voice_mail_message",
                "welcome_message_is_generated": True,
            },
            llm_config={
                "model": "model",
                "provider": "openai",
                "frequency_penalty": -2,
                "max_tokens": 1,
                "parallel_tool_calls": True,
                "presence_penalty": -2,
                "system_prompt": "system_prompt",
                "temperature": 0,
                "top_k": 1,
                "top_p": 0,
            },
            plugins=[{}],
            precall_webhook={
                "method": "GET",
                "url": "url",
                "body_template": {"foo": "bar"},
                "headers": {"foo": "string"},
                "timeout_seconds": 1,
            },
            room_duration_config={
                "close_room_message": "close_room_message",
                "duration_warning_message": "duration_warning_message",
                "max_duration_min": 1,
                "max_silence_sec": 0,
                "silence_message": "silence_message",
                "wait_for_message_sec": 0,
            },
            transcriber_config={
                "provider": "deepgram",
                "commit_strategy": "manual",
                "detect_language": True,
                "eager_eot_threshold": 0,
                "enable_logging": True,
                "endpointing": 0,
                "endpointing_ms": 0,
                "energy_filter": True,
                "eot_threshold": 0,
                "eot_timeout_ms": 0,
                "filler_words": True,
                "include_language_detection": True,
                "include_timestamps": True,
                "interim_results": True,
                "keyterms": ["string"],
                "keywords": ["string"],
                "language": "language",
                "language_code": "language_code",
                "min_speech_duration_ms": 0,
                "model": "model",
                "no_delay": True,
                "num_channels": 1,
                "preemptive_generation": True,
                "preemptive_min_confidence": 0,
                "profanity_filter": True,
                "punctuate": True,
                "sample_rate": 8000,
                "smart_format": True,
                "vad_events": True,
            },
            vad_config={
                "activation_threshold": 0,
                "max_buffered_speech": 1,
                "min_silence_duration": 0,
                "min_speech_duration": 0,
                "prefix_padding_duration": 0,
                "sample_rate": 8000,
            },
            voice_config={
                "model": "model",
                "provider": "provider",
                "language": "language",
                "sample_rate": 8000,
                "similarity_boost": 0,
                "speed": 0.1,
                "stability": 0,
                "style": 0,
                "use_speaker_boost": True,
                "voice_id": "voice_id",
            },
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Cozmoai) -> None:
        response = client.agents.with_raw_response.create(
            org_id="org_id",
            name="name",
            prompt_template="prompt_template",
            type="voice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Cozmoai) -> None:
        with client.agents.with_streaming_response.create(
            org_id="org_id",
            name="name",
            prompt_template="prompt_template",
            type="voice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.agents.with_raw_response.create(
                org_id="",
                name="name",
                prompt_template="prompt_template",
                type="voice",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Cozmoai) -> None:
        agent = client.agents.retrieve(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Cozmoai) -> None:
        response = client.agents.with_raw_response.retrieve(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Cozmoai) -> None:
        with client.agents.with_streaming_response.retrieve(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.agents.with_raw_response.retrieve(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.retrieve(
                agent_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Cozmoai) -> None:
        agent = client.agents.update(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Cozmoai) -> None:
        agent = client.agents.update(
            agent_id="agent_id",
            org_id="org_id",
            allowed_sip_trunks=["string"],
            background_sound={
                "file": "file",
                "enabled": True,
                "initial_volume": 0,
                "thinking_sound": [
                    {
                        "sound": "sound",
                        "probability": 0,
                        "volume": 0,
                    }
                ],
                "volume": 0,
            },
            extra_config={
                "allow_interruptions": True,
                "interruption_sensitivity": 0,
                "min_words": 0,
                "turn_detector_enabled": True,
                "turn_detector_is_multilingual": True,
                "turn_detector_model_type": "turn_detector_model_type",
            },
            goodbye_config={
                "enabled": True,
                "message": "message",
            },
            greeting_config={
                "agent_speaks_first": True,
                "greeting": "greeting",
                "pause_before_first_message": 0,
                "voice_mail_message": "voice_mail_message",
                "welcome_message_is_generated": True,
            },
            llm_config={
                "model": "model",
                "provider": "openai",
                "frequency_penalty": -2,
                "max_tokens": 1,
                "parallel_tool_calls": True,
                "presence_penalty": -2,
                "system_prompt": "system_prompt",
                "temperature": 0,
                "top_k": 1,
                "top_p": 0,
            },
            name="name",
            plugins=[{}],
            precall_webhook={
                "method": "GET",
                "url": "url",
                "body_template": {"foo": "bar"},
                "headers": {"foo": "string"},
                "timeout_seconds": 1,
            },
            prompt_template="prompt_template",
            room_duration_config={
                "close_room_message": "close_room_message",
                "duration_warning_message": "duration_warning_message",
                "max_duration_min": 1,
                "max_silence_sec": 0,
                "silence_message": "silence_message",
                "wait_for_message_sec": 0,
            },
            transcriber_config={
                "provider": "deepgram",
                "commit_strategy": "manual",
                "detect_language": True,
                "eager_eot_threshold": 0,
                "enable_logging": True,
                "endpointing": 0,
                "endpointing_ms": 0,
                "energy_filter": True,
                "eot_threshold": 0,
                "eot_timeout_ms": 0,
                "filler_words": True,
                "include_language_detection": True,
                "include_timestamps": True,
                "interim_results": True,
                "keyterms": ["string"],
                "keywords": ["string"],
                "language": "language",
                "language_code": "language_code",
                "min_speech_duration_ms": 0,
                "model": "model",
                "no_delay": True,
                "num_channels": 1,
                "preemptive_generation": True,
                "preemptive_min_confidence": 0,
                "profanity_filter": True,
                "punctuate": True,
                "sample_rate": 8000,
                "smart_format": True,
                "vad_events": True,
            },
            type="voice",
            vad_config={
                "activation_threshold": 0,
                "max_buffered_speech": 1,
                "min_silence_duration": 0,
                "min_speech_duration": 0,
                "prefix_padding_duration": 0,
                "sample_rate": 8000,
            },
            voice_config={
                "model": "model",
                "provider": "provider",
                "language": "language",
                "sample_rate": 8000,
                "similarity_boost": 0,
                "speed": 0.1,
                "stability": 0,
                "style": 0,
                "use_speaker_boost": True,
                "voice_id": "voice_id",
            },
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Cozmoai) -> None:
        response = client.agents.with_raw_response.update(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Cozmoai) -> None:
        with client.agents.with_streaming_response.update(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.agents.with_raw_response.update(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.update(
                agent_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Cozmoai) -> None:
        agent = client.agents.list(
            org_id="org_id",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Cozmoai) -> None:
        agent = client.agents.list(
            org_id="org_id",
            page=0,
            search="search",
            size=0,
            type="type",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Cozmoai) -> None:
        response = client.agents.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Cozmoai) -> None:
        with client.agents.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.agents.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Cozmoai) -> None:
        agent = client.agents.delete(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Cozmoai) -> None:
        response = client.agents.with_raw_response.delete(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Cozmoai) -> None:
        with client.agents.with_streaming_response.delete(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentDeleteResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Cozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.agents.with_raw_response.delete(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                agent_id="",
                org_id="org_id",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCozmoai) -> None:
        agent = await async_client.agents.create(
            org_id="org_id",
            name="name",
            prompt_template="prompt_template",
            type="voice",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCozmoai) -> None:
        agent = await async_client.agents.create(
            org_id="org_id",
            name="name",
            prompt_template="prompt_template",
            type="voice",
            allowed_sip_trunks=["string"],
            background_sound={
                "file": "file",
                "enabled": True,
                "initial_volume": 0,
                "thinking_sound": [
                    {
                        "sound": "sound",
                        "probability": 0,
                        "volume": 0,
                    }
                ],
                "volume": 0,
            },
            extra_config={
                "allow_interruptions": True,
                "interruption_sensitivity": 0,
                "min_words": 0,
                "turn_detector_enabled": True,
                "turn_detector_is_multilingual": True,
                "turn_detector_model_type": "turn_detector_model_type",
            },
            goodbye_config={
                "enabled": True,
                "message": "message",
            },
            greeting_config={
                "agent_speaks_first": True,
                "greeting": "greeting",
                "pause_before_first_message": 0,
                "voice_mail_message": "voice_mail_message",
                "welcome_message_is_generated": True,
            },
            llm_config={
                "model": "model",
                "provider": "openai",
                "frequency_penalty": -2,
                "max_tokens": 1,
                "parallel_tool_calls": True,
                "presence_penalty": -2,
                "system_prompt": "system_prompt",
                "temperature": 0,
                "top_k": 1,
                "top_p": 0,
            },
            plugins=[{}],
            precall_webhook={
                "method": "GET",
                "url": "url",
                "body_template": {"foo": "bar"},
                "headers": {"foo": "string"},
                "timeout_seconds": 1,
            },
            room_duration_config={
                "close_room_message": "close_room_message",
                "duration_warning_message": "duration_warning_message",
                "max_duration_min": 1,
                "max_silence_sec": 0,
                "silence_message": "silence_message",
                "wait_for_message_sec": 0,
            },
            transcriber_config={
                "provider": "deepgram",
                "commit_strategy": "manual",
                "detect_language": True,
                "eager_eot_threshold": 0,
                "enable_logging": True,
                "endpointing": 0,
                "endpointing_ms": 0,
                "energy_filter": True,
                "eot_threshold": 0,
                "eot_timeout_ms": 0,
                "filler_words": True,
                "include_language_detection": True,
                "include_timestamps": True,
                "interim_results": True,
                "keyterms": ["string"],
                "keywords": ["string"],
                "language": "language",
                "language_code": "language_code",
                "min_speech_duration_ms": 0,
                "model": "model",
                "no_delay": True,
                "num_channels": 1,
                "preemptive_generation": True,
                "preemptive_min_confidence": 0,
                "profanity_filter": True,
                "punctuate": True,
                "sample_rate": 8000,
                "smart_format": True,
                "vad_events": True,
            },
            vad_config={
                "activation_threshold": 0,
                "max_buffered_speech": 1,
                "min_silence_duration": 0,
                "min_speech_duration": 0,
                "prefix_padding_duration": 0,
                "sample_rate": 8000,
            },
            voice_config={
                "model": "model",
                "provider": "provider",
                "language": "language",
                "sample_rate": 8000,
                "similarity_boost": 0,
                "speed": 0.1,
                "stability": 0,
                "style": 0,
                "use_speaker_boost": True,
                "voice_id": "voice_id",
            },
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.agents.with_raw_response.create(
            org_id="org_id",
            name="name",
            prompt_template="prompt_template",
            type="voice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCozmoai) -> None:
        async with async_client.agents.with_streaming_response.create(
            org_id="org_id",
            name="name",
            prompt_template="prompt_template",
            type="voice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.agents.with_raw_response.create(
                org_id="",
                name="name",
                prompt_template="prompt_template",
                type="voice",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCozmoai) -> None:
        agent = await async_client.agents.retrieve(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCozmoai) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                agent_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCozmoai) -> None:
        agent = await async_client.agents.update(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCozmoai) -> None:
        agent = await async_client.agents.update(
            agent_id="agent_id",
            org_id="org_id",
            allowed_sip_trunks=["string"],
            background_sound={
                "file": "file",
                "enabled": True,
                "initial_volume": 0,
                "thinking_sound": [
                    {
                        "sound": "sound",
                        "probability": 0,
                        "volume": 0,
                    }
                ],
                "volume": 0,
            },
            extra_config={
                "allow_interruptions": True,
                "interruption_sensitivity": 0,
                "min_words": 0,
                "turn_detector_enabled": True,
                "turn_detector_is_multilingual": True,
                "turn_detector_model_type": "turn_detector_model_type",
            },
            goodbye_config={
                "enabled": True,
                "message": "message",
            },
            greeting_config={
                "agent_speaks_first": True,
                "greeting": "greeting",
                "pause_before_first_message": 0,
                "voice_mail_message": "voice_mail_message",
                "welcome_message_is_generated": True,
            },
            llm_config={
                "model": "model",
                "provider": "openai",
                "frequency_penalty": -2,
                "max_tokens": 1,
                "parallel_tool_calls": True,
                "presence_penalty": -2,
                "system_prompt": "system_prompt",
                "temperature": 0,
                "top_k": 1,
                "top_p": 0,
            },
            name="name",
            plugins=[{}],
            precall_webhook={
                "method": "GET",
                "url": "url",
                "body_template": {"foo": "bar"},
                "headers": {"foo": "string"},
                "timeout_seconds": 1,
            },
            prompt_template="prompt_template",
            room_duration_config={
                "close_room_message": "close_room_message",
                "duration_warning_message": "duration_warning_message",
                "max_duration_min": 1,
                "max_silence_sec": 0,
                "silence_message": "silence_message",
                "wait_for_message_sec": 0,
            },
            transcriber_config={
                "provider": "deepgram",
                "commit_strategy": "manual",
                "detect_language": True,
                "eager_eot_threshold": 0,
                "enable_logging": True,
                "endpointing": 0,
                "endpointing_ms": 0,
                "energy_filter": True,
                "eot_threshold": 0,
                "eot_timeout_ms": 0,
                "filler_words": True,
                "include_language_detection": True,
                "include_timestamps": True,
                "interim_results": True,
                "keyterms": ["string"],
                "keywords": ["string"],
                "language": "language",
                "language_code": "language_code",
                "min_speech_duration_ms": 0,
                "model": "model",
                "no_delay": True,
                "num_channels": 1,
                "preemptive_generation": True,
                "preemptive_min_confidence": 0,
                "profanity_filter": True,
                "punctuate": True,
                "sample_rate": 8000,
                "smart_format": True,
                "vad_events": True,
            },
            type="voice",
            vad_config={
                "activation_threshold": 0,
                "max_buffered_speech": 1,
                "min_silence_duration": 0,
                "min_speech_duration": 0,
                "prefix_padding_duration": 0,
                "sample_rate": 8000,
            },
            voice_config={
                "model": "model",
                "provider": "provider",
                "language": "language",
                "sample_rate": 8000,
                "similarity_boost": 0,
                "speed": 0.1,
                "stability": 0,
                "style": 0,
                "use_speaker_boost": True,
                "voice_id": "voice_id",
            },
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.agents.with_raw_response.update(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCozmoai) -> None:
        async with async_client.agents.with_streaming_response.update(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.agents.with_raw_response.update(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.update(
                agent_id="",
                org_id="org_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCozmoai) -> None:
        agent = await async_client.agents.list(
            org_id="org_id",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCozmoai) -> None:
        agent = await async_client.agents.list(
            org_id="org_id",
            page=0,
            search="search",
            size=0,
            type="type",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.agents.with_raw_response.list(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCozmoai) -> None:
        async with async_client.agents.with_streaming_response.list(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.agents.with_raw_response.list(
                org_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCozmoai) -> None:
        agent = await async_client.agents.delete(
            agent_id="agent_id",
            org_id="org_id",
        )
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCozmoai) -> None:
        response = await async_client.agents.with_raw_response.delete(
            agent_id="agent_id",
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentDeleteResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCozmoai) -> None:
        async with async_client.agents.with_streaming_response.delete(
            agent_id="agent_id",
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentDeleteResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCozmoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                agent_id="agent_id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                agent_id="",
                org_id="org_id",
            )
