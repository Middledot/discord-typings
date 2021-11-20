from __future__ import annotations

from typing import Optional

from typing_extensions import NotRequired, TypedDict, Literal

__all__ = ('UserData',)


class UserConnection(TypedDict):
    id: str
    name: str
    type: Literal['twitch', 'youtube']
    revoked: NotRequired[bool]


class UserData(TypedDict):
    id: str
    username: str
    discriminator: str
    avatar: Optional[str]
    bot: NotRequired[bool]
    system: NotRequired[bool]
    mfa_enabled: NotRequired[bool]
    banner: NotRequired[Optional[str]]
    accent_color: NotRequired[Optional[int]]
    locale: NotRequired[str]
    verified: NotRequired[bool]
    email: NotRequired[Optional[bool]]
    flags: NotRequired[int]
    premium_type: NotRequired[Literal[0, 1, 2]]
    public_flags: NotRequired[int]