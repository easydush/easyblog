import faker from "@faker-js/faker";

export const getFakePost = () => {
    return {
        title: faker.lorem.sentence(),
        comments: [],
        description: faker.lorem.paragraph()
    }
}

export const getFakeComment = (id, isPost) => {
    return {
        text: faker.lorem.sentence(),
        post: isPost ? id : null,
        parent_comment: isPost ? null : id,
    }
}