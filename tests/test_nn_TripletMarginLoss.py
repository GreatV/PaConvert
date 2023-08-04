# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
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

import textwrap

from apibase import APIBase

obj = APIBase("torch.nn.TripletMarginLoss")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 5, 3], [0, 3, 2], [1, 4, 1]]).type(torch.float32)
        positive= torch.Tensor([[5, 1, 2], [3, 2, 1], [3, -1, 1]]).type(torch.float32)
        negative = torch.Tensor([[2, 1, -3], [1, 1, -1], [4, -2, 1]]).type(torch.float32)
        cri = torch.nn.TripletMarginLoss()
        result = cri(input, positive, negative)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 5, 3], [0, 3, 2], [1, 4, 1]]).type(torch.float32)
        positive= torch.Tensor([[5, 1, 2], [3, 2, 1], [3, -1, 1]]).type(torch.float32)
        negative = torch.Tensor([[2, 1, -3], [1, 1, -1], [4, -2, 1]]).type(torch.float32)
        cri = torch.nn.TripletMarginLoss(1.3, 3.2, 1e-5, False, True, False, reduction='mean')
        result = cri(input, positive, negative)
        """
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5, atol=1.0e-8)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 5, 3], [0, 3, 2], [1, 4, 1]]).type(torch.float32)
        positive= torch.Tensor([[5, 1, 2], [3, 2, 1], [3, -1, 1]]).type(torch.float32)
        negative = torch.Tensor([[2, 1, -3], [1, 1, -1], [4, -2, 1]]).type(torch.float32)
        cri = torch.nn.TripletMarginLoss(1.3, 3.2, 1e-5, True, True, True, reduction='sum')
        result = cri(input, positive, negative)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 5, 3], [0, 3, 2], [1, 4, 1]]).type(torch.float32)
        positive= torch.Tensor([[5, 1, 2], [3, 2, 1], [3, -1, 1]]).type(torch.float32)
        negative = torch.Tensor([[2, 1, -3], [1, 1, -1], [4, -2, 1]]).type(torch.float32)
        cri = torch.nn.TripletMarginLoss(1.3, 3.2, 1e-5, False, False, True, reduction='mean')
        result = cri(input, positive, negative)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 5, 3], [0, 3, 2], [1, 4, 1]]).type(torch.float32)
        positive= torch.Tensor([[5, 1, 2], [3, 2, 1], [3, -1, 1]]).type(torch.float32)
        negative = torch.Tensor([[2, 1, -3], [1, 1, -1], [4, -2, 1]]).type(torch.float32)
        cri = torch.nn.TripletMarginLoss(1.3, 3.2, 1e-5, True, True, False, reduction='none')
        result = cri(input, positive, negative)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 5, 3], [0, 3, 2], [1, 4, 1]]).type(torch.float32)
        positive= torch.Tensor([[5, 1, 2], [3, 2, 1], [3, -1, 1]]).type(torch.float32)
        negative = torch.Tensor([[2, 1, -3], [1, 1, -1], [4, -2, 1]]).type(torch.float32)
        cri = torch.nn.TripletMarginLoss(1.3, 3.2, 1e-5, False, False, False, reduction='sum')
        result = cri(input, positive, negative)
        """
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5, atol=1.0e-8)


def test_case_7():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 5, 3], [0, 3, 2], [1, 4, 1]]).type(torch.float32)
        positive= torch.Tensor([[5, 1, 2], [3, 2, 1], [3, -1, 1]]).type(torch.float32)
        negative = torch.Tensor([[2, 1, -3], [1, 1, -1], [4, -2, 1]]).type(torch.float32)
        cri = torch.nn.TripletMarginLoss(1.3, 3.2, 1e-5, True, True, False, reduction='mean')
        result = cri(input, positive, negative)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_8():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 5, 3], [0, 3, 2], [1, 4, 1]]).type(torch.float32)
        positive= torch.Tensor([[5, 1, 2], [3, 2, 1], [3, -1, 1]]).type(torch.float32)
        negative = torch.Tensor([[2, 1, -3], [1, 1, -1], [4, -2, 1]]).type(torch.float32)
        cri = torch.nn.TripletMarginLoss(1.3, 3.2, 1e-5, True, False, True, reduction='mean')
        result = cri(input, positive, negative)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_9():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.Tensor([[1, 5, 3], [0, 3, 2], [1, 4, 1]]).type(torch.float32)
        positive= torch.Tensor([[5, 1, 2], [3, 2, 1], [3, -1, 1]]).type(torch.float32)
        negative = torch.Tensor([[2, 1, -3], [1, 1, -1], [4, -2, 1]]).type(torch.float32)
        cri = torch.nn.TripletMarginLoss(1.3, 3.2, 1e-1, False, True, False, reduction='mean')
        result = cri(input, positive, negative)
        """
    )
    obj.run(pytorch_code, ["result"], rtol=1.0e-5, atol=1.0e-8)
