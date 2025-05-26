import React, { useState } from "react";
import axios from "axios";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";


export default function App() {
  const [tickers, setTickers] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://localhost:8000/analyze", {
        tickers,
        language: "zh"
      });
      if (typeof response.data.summary === "string") {
        setResult(response.data.summary);
      } else {
        setResult(JSON.stringify(response.data.summary, null, 2));
      }
    } catch (error) {
      setResult("请求失败，请检查服务是否启动。");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="max-w-xl mx-auto">
        <Card>
          <CardContent className="space-y-4">
            <h1 className="text-xl font-bold">股票分析系统</h1>
            {/* ✅ 修改：添加 Label，提示中国市场股票代码格式 */}
            <Label htmlFor="ticker-input">股票代码（中国市场，附交易所后缀）</Label>
            {/* ✅ 修改：更新 placeholder 示例为中国市场代码 */}
            <Input
              id="ticker-input"
              placeholder="例如：000001.SZ,600000.SH"
              value={tickers}
              onChange={(e) => setTickers(e.target.value)}
            />
            <Button onClick={handleAnalyze} disabled={loading}>
              {loading ? "分析中..." : "开始分析"}
            </Button>
          </CardContent>
        </Card>

        {result && (
          <Card className="mt-4">
            <CardContent>
              {/* ✅ 修改：使用 Textarea 显示结果，支持多行 */}
              <Textarea
                className="whitespace-pre-wrap text-sm text-gray-700"
                rows={12}
                value={result}
                readOnly
              />
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}
