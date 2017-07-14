# Copyright 2017 PHONEMETRA. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================


.PHONY: env env-dev

# Virtual environment creation and deps install.
env:
	conda create -y -n QISKitenv python=3 pip
	bash -c "source activate QISKitenv;pip install -r requires.txt"

env-dev: env
	bash -c "source activate QISKitenv;pip install pylint matplotlib"

run: 
	bash -c "source activate QISKitenv;cd turbo;python turbo.py"