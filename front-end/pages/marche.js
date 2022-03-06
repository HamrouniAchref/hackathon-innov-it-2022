import Head from "next/head";

import Layout from "../components/layout";
import Jumbotron from "../components/jumbotron";
import { getPageData } from "../lib/api";
import { CMS_NAME } from "../lib/constants";

export default function ValuesPage({ page }) {
  return (
    <>
      <Layout>
        <Head>
          <title>Values | {CMS_NAME}</title>
        </Head>
        <Jumbotron
          title={page.title}
          subtitle={page.subtitle}
          imageUrl={page.image}
        />
        <div className="mw7 center ph3 pt4" style={{ margin: "4rem auto" }}>
          {page.values.map((v, i) => (
            <MediaBlock
              key={v.heading}
              heading={v.heading}
              text={v.text}
              imageUrl={v.imageUrl}
              reverse={i % 2 == 0}
            />
          ))}
        </div>
      </Layout>
    </>
  );
}

export async function getStaticProps() {
  const page = getPageData("marche");
  return {
    props: { page },
  };
}

function MediaBlock({ imageUrl, heading, text, reverse }) {
  return (
    <div className="flex-m mhn3-m mb4" style={{ alignItems: "center" }}>
      <div className={`ph3-m w-50-m ${reverse && "order-last-m"}`}>
        <img src={imageUrl} alt="value image" className="db mb2" />
      </div>
      <div
        className="ph3-m w-50-m"
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          textAlign: "center",
        }}
      >
        <h3 className="f4 b lh-title mb1 center">{heading}</h3>

        <div style={{ position: "relative" }}>
          <p
            className="primary tc lh-title tunaa"
            style={{
              position: "relative",
              display: "inline-block",
              marginRight: "1rem",
            }}
          >
            80
            <span className="f4">Dt</span>
          </p>
          <p className="primary f4 b tc " style={{ display: "inline-block" }}>
            59
            <span className="f4">Dt</span>
          </p>
          <p style={{ textAlign: "center" }}>{text}</p>
        </div>
        <div
          style={{
            width: "100%",
            marginBottom: "2rem",
            display: "flex",
            justifyContent: "center",
          }}
        >
          <button
            style={{
              fontSize: "1rem",
              padding: "1rem",
              background: "#44ad44",
              color: "white",
            }}
          >
            Achat
          </button>
        </div>
      </div>
    </div>
  );
}
