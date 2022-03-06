import Head from "next/head";

import Layout from "../components/layout";
import Jumbotron from "../components/jumbotron";
import MediaBlock from "../components/media-block";
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
        <div style={{ padding: "10rem" }}>
          {page.values.map((v, i) => (
            <MediaBlock
              key={v.heading1}
              heading1={v.heading1}
              text1={v.text1}
              heading2={v.heading2}
              text2={v.text2}
              heading3={v.heading3}
              text3={v.text3}
              heading4={v.heading4}
              text4={v.text4}
              imageUrl={v.imageUrl}
              // reverse={i % 2 == 0}
            />
          ))}
        </div>
      </Layout>
    </>
  );
}

export async function getStaticProps() {
  const page = getPageData("values");
  return {
    props: { page },
  };
}
