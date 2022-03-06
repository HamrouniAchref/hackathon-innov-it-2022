import Head from "next/head";

import Layout from "../components/layout";
import Jumbotron from "../components/jumbotron";
import ShortText from "../components/short-text";
import TwoUp from "../components/2-up";
import TextAndImage from "../components/text-and-image";
import Blog4Home from "../components/blog-4-home";

import { getHomePageData, getPosts4Home } from "../lib/api";
import { CMS_NAME } from "../lib/constants";

import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend,
} from "chart.js";
import { Radar } from "react-chartjs-2";

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);

export const data = {
  labels: ["Thing 1", "Thing 2", "Thing 3", "Thing 4", "Thing 5", "Thing 6"],
  datasets: [
    {
      label: "# of Votes",
      data: [2, 9, 3, 5, 2, 3],
      backgroundColor: "rgba(255, 99, 132, 0.2)",
      borderColor: "rgba(255, 99, 132, 1)",
      borderWidth: 1,
    },
  ],
};

export default function Index({ homeData, posts }) {
  return (
    <>
      <Layout>
        <Head>
          <title>Home | {CMS_NAME}</title>
        </Head>
        <Jumbotron
          title={homeData.title}
          subtitle={homeData.subtitle}
          imageUrl={homeData.image}
        />
        <div
          style={{
            padding: "2rem",
            display: "flex",
            justifyContent: "center",
          }}
        >
          <div
            style={{
              width: "20rem",
              height: "20rem",
            }}
          >
            <Radar data={data} />
          </div>
        </div>
        <ShortText
          heading={homeData.blurb.heading}
          text={homeData.blurb.text}
        />
        <TwoUp intro={homeData.intro} products={homeData.products} />
        <TextAndImage
          heading={homeData.values.heading}
          text={homeData.values.text}
          buttonText={homeData.values.buttonText}
          buttonLink={homeData.values.buttonLink}
          image={homeData.values.image}
        />
        <Blog4Home posts={posts} />
      </Layout>
    </>
  );
}

export async function getStaticProps() {
  const homeData = getHomePageData();
  const posts = getPosts4Home();
  return {
    props: { homeData, posts },
  };
}
