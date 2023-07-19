import axios from "axios";

export const config = {
  api: {
    bodyParser: false,
  },
};


async function handler(req: any, res: any) {
  const baseUrl = "https://www.muganedev.tech/api/v1/";

  if (req.method == "POST") {
    const { data } = await axios.post(`${baseUrl}complaints/create`,
      req, {
      responseType: "stream",
      headers: {
        'Content-Type': req.headers["content-type"],
        'Authorization': req.headers["authorization"],
      },
    });
    data.pipe(res);
    return res.status(200).json(data);
  } else {
    return res.status(502).json({ message: "Bad Gateway" });
  }
}

export default handler;
