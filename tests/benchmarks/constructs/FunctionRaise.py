#     Copyright 2017, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Python test originally created or extracted from other peoples work. The
#     parts from me are licensed as below. It is at least Free Software where
#     it's copied from other people. In these cases, that will normally be
#     indicated.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#

from __future__ import print_function

count = 0

def raisy():
    global count
    count += 1

    raise TypeError

def calledRepeatedly():
# construct_begin
    try:
        raisy()
    except TypeError:
        pass
# construct_alternative
    pass
# construct_end

for x in xrange(50000):
    calledRepeatedly()

# construct_begin
assert count == 50000
# construct_alternative
assert count == 0
# construct_end
print("OK.")
