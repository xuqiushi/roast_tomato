export interface PreviewBlogContent {
  id: string;
  name: string;
  summary: string;
  createAt: number;
}
export interface PaginationPara {
  countAll: number,
  selectNow: number,
}
export interface BlogDetail {
  id: string;
  name: string;
  userId: string;
  content: string;
  creatAt: number;
}
export interface BlogCodeMirrorStructure {
  codeTitle: string;
  codeSummary: string;
  codeContent: string;
}
export interface BlogComment {
  id: string;
  content: string;
  userId: string;
  userName: string;
  userMainImage: string;
  creatAt: number;
}
export interface BlogManageRecord {
  name: string;
  userName: string;
  creatAt: number;
}