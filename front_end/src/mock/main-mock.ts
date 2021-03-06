import Mock from 'mockjs'
export let start_mock = () => {
  Mock.mock(
    /api\/blog_list/,
    'post',
    {
      'previewBlogList|8': [
        {
          "id": "@string(20)",
          "name": '@title',
          "summary": '@cparagraph(5)',
          "createAt": '@integer(10)',
        }
      ]
    },
  )
  Mock.mock(
      /api\/get_blog_pagination_count/,
      'post',
      {
          "countAll|50-200": 100,
      },
  )
  Mock.mock(
    /api\/blog\/[^\/]*$/,
    'post',
    {
      "id": "@string(20)",
      "name": '@title',
      "userId": '@string(20)',
      "content": '@cparagraph(50)',
      "createAt": '@integer(10)',
    },
  )
  Mock.mock(
    /api\/blog_comment\/.*/,
    'post',
    [
      {
        "id": "@string(20)",
        "content": '@cparagraph(1)',
        "userId": '@string(20)',
        "userName": '@cname',
        "userMainImage": '@image(200x200)',
        "createAt": '@integer(10)',
      },
      {
        "id": "@string(20)",
        "content": '@cparagraph(1)',
        "userId": '@string(20)',
        "userName": '@cname',
        "userMainImage": '@image(200x200)',
        "createAt": '@integer(10)',
      },
      {
        "id": "@string(20)",
        "content": '@cparagraph(1)',
        "userId": '@string(20)',
        "userName": '@cname',
        "userMainImage": '@image(200x200)',
        "createAt": '@integer(10)',
      },
    ],
  )
  Mock.mock(
    /api\/users\/.*/,
    'post',
    {
      "id": "@string(20)",
      "userName": '@cname',
      "userMainImage": '@image(200x200)',
    },
  )
  Mock.mock(
    /api\/users\/current_user/,
    'post',
    {
      "id": "@string(20)",
      "userName": '@cname',
      "userMainImage": '@image(200x200)',
    }
  )
  Mock.mock(
    /api\/blog\/manage\/get_list/,
    'post',
    {
      'blogManageRecords|20': [
        {
          "id": "@string(20)",
          "name": '@title',
          "userName": '@cname',
          "createAt": '@integer(10)',
        }
      ]
    }
  )
}
