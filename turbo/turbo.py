
# Copyright 2017 PHONEMETRA All Rights Reserved.
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

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from qiskit import QuantumProgram

# We need the environment variable for Travis.
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    import Qconfig
    API_TOKEN = Qconfig.APItoken
    URL = Qconfig.config["url"]
except ImportError:
    API_TOKEN = os.environ["QE_TOKEN"]
    URL = os.environ["QE_URL"]


class TurboAI(object):
    def setup_api(self):
        QP_program = QuantumProgram()
        result = QP_program.set_api(API_TOKEN, URL)
        print('setup_api:' + result)
        return result
        
        

    def main():
         
        if __name__ == '__main__': 
            main()
        
        
