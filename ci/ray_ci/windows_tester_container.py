from typing import List, Optional

from ci.ray_ci.windows_container import WindowsContainer
from ci.ray_ci.tester_container import TesterContainer


class WindowsTesterContainer(TesterContainer, WindowsContainer):
    def __init__(
        self,
        docker_tag: str,
        shard_count: int = 1,
        gpus: int = 0,
        test_envs: Optional[List[str]] = None,
        shard_ids: Optional[List[int]] = None,
        skip_ray_installation: bool = False,
        build_type: Optional[str] = None,
    ) -> None:
        WindowsContainer.__init__(
            self,
            docker_tag,
            envs=test_envs,
        )
        TesterContainer.__init__(
            self,
            shard_count,
            gpus,
            test_envs=test_envs,
            shard_ids=shard_ids,
            skip_ray_installation=skip_ray_installation,
            build_type=build_type,
        )
