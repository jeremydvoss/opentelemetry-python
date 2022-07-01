# Copyright The OpenTelemetry Authors
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

from flask import Flask, request
from os import environ
from opentelemetry.environment_variables import (
    OTEL_METRICS_EXPORTER,
    OTEL_TRACES_EXPORTER,
)

app = Flask(__name__)


@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    return "served"


if __name__ == "__main__":
    print("JEREMYVOSS: server_uninstrumented")
    print("JEREMYVOSS: PYTHONPATH: %s" % environ["PYTHONPATH"])
    print("JEREMYVOSS: OTEL_TRACES_EXPORTER: %s" % environ[OTEL_TRACES_EXPORTER])
    # print("JEREMYVOSS: OTEL_METRICS_EXPORTER: %s" % environ[OTEL_METRICS_EXPORTER])
    app.run(port=8082)
