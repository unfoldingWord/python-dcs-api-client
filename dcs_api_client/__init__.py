# coding: utf-8

# flake8: noqa

"""
    DCS (Gitea) API.

    This documentation describes the DCS (Gitea) API.  # noqa: E501

    OpenAPI spec version: 1.15.9+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from dcs_api_client.api.admin_api import AdminApi
from dcs_api_client.api.issue_api import IssueApi
from dcs_api_client.api.miscellaneous_api import MiscellaneousApi
from dcs_api_client.api.notification_api import NotificationApi
from dcs_api_client.api.organization_api import OrganizationApi
from dcs_api_client.api.repository_api import RepositoryApi
from dcs_api_client.api.settings_api import SettingsApi
from dcs_api_client.api.user_api import UserApi

# import ApiClient
from dcs_api_client.api_client import ApiClient
from dcs_api_client.configuration import Configuration
# import models into sdk package
from dcs_api_client.models.api_error import APIError
from dcs_api_client.models.access_token import AccessToken
from dcs_api_client.models.add_collaborator_option import AddCollaboratorOption
from dcs_api_client.models.add_time_option import AddTimeOption
from dcs_api_client.models.annotated_tag import AnnotatedTag
from dcs_api_client.models.annotated_tag_object import AnnotatedTagObject
from dcs_api_client.models.attachment import Attachment
from dcs_api_client.models.branch import Branch
from dcs_api_client.models.branch_protection import BranchProtection
from dcs_api_client.models.catalog_stage import CatalogStage
from dcs_api_client.models.catalog_stages import CatalogStages
from dcs_api_client.models.combined_status import CombinedStatus
from dcs_api_client.models.comment import Comment
from dcs_api_client.models.commit import Commit
from dcs_api_client.models.commit_affected_files import CommitAffectedFiles
from dcs_api_client.models.commit_date_options import CommitDateOptions
from dcs_api_client.models.commit_meta import CommitMeta
from dcs_api_client.models.commit_status import CommitStatus
from dcs_api_client.models.commit_status_state import CommitStatusState
from dcs_api_client.models.commit_user import CommitUser
from dcs_api_client.models.contents_response import ContentsResponse
from dcs_api_client.models.create_access_token_option import CreateAccessTokenOption
from dcs_api_client.models.create_branch_protection_option import CreateBranchProtectionOption
from dcs_api_client.models.create_branch_repo_option import CreateBranchRepoOption
from dcs_api_client.models.create_email_option import CreateEmailOption
from dcs_api_client.models.create_file_options import CreateFileOptions
from dcs_api_client.models.create_fork_option import CreateForkOption
from dcs_api_client.models.create_gpg_key_option import CreateGPGKeyOption
from dcs_api_client.models.create_hook_option import CreateHookOption
from dcs_api_client.models.create_hook_option_config import CreateHookOptionConfig
from dcs_api_client.models.create_issue_comment_option import CreateIssueCommentOption
from dcs_api_client.models.create_issue_option import CreateIssueOption
from dcs_api_client.models.create_key_option import CreateKeyOption
from dcs_api_client.models.create_label_option import CreateLabelOption
from dcs_api_client.models.create_milestone_option import CreateMilestoneOption
from dcs_api_client.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from dcs_api_client.models.create_org_option import CreateOrgOption
from dcs_api_client.models.create_pull_request_option import CreatePullRequestOption
from dcs_api_client.models.create_pull_review_comment import CreatePullReviewComment
from dcs_api_client.models.create_pull_review_options import CreatePullReviewOptions
from dcs_api_client.models.create_release_option import CreateReleaseOption
from dcs_api_client.models.create_repo_option import CreateRepoOption
from dcs_api_client.models.create_status_option import CreateStatusOption
from dcs_api_client.models.create_tag_option import CreateTagOption
from dcs_api_client.models.create_team_option import CreateTeamOption
from dcs_api_client.models.create_user_option import CreateUserOption
from dcs_api_client.models.cron import Cron
from dcs_api_client.models.delete_email_option import DeleteEmailOption
from dcs_api_client.models.delete_file_options import DeleteFileOptions
from dcs_api_client.models.deploy_key import DeployKey
from dcs_api_client.models.dismiss_pull_review_options import DismissPullReviewOptions
from dcs_api_client.models.edit_attachment_options import EditAttachmentOptions
from dcs_api_client.models.edit_branch_protection_option import EditBranchProtectionOption
from dcs_api_client.models.edit_deadline_option import EditDeadlineOption
from dcs_api_client.models.edit_git_hook_option import EditGitHookOption
from dcs_api_client.models.edit_hook_option import EditHookOption
from dcs_api_client.models.edit_issue_comment_option import EditIssueCommentOption
from dcs_api_client.models.edit_issue_option import EditIssueOption
from dcs_api_client.models.edit_label_option import EditLabelOption
from dcs_api_client.models.edit_milestone_option import EditMilestoneOption
from dcs_api_client.models.edit_org_option import EditOrgOption
from dcs_api_client.models.edit_pull_request_option import EditPullRequestOption
from dcs_api_client.models.edit_reaction_option import EditReactionOption
from dcs_api_client.models.edit_release_option import EditReleaseOption
from dcs_api_client.models.edit_repo_option import EditRepoOption
from dcs_api_client.models.edit_team_option import EditTeamOption
from dcs_api_client.models.edit_user_option import EditUserOption
from dcs_api_client.models.email import Email
from dcs_api_client.models.external_tracker import ExternalTracker
from dcs_api_client.models.external_wiki import ExternalWiki
from dcs_api_client.models.file_commit_response import FileCommitResponse
from dcs_api_client.models.file_delete_response import FileDeleteResponse
from dcs_api_client.models.file_links_response import FileLinksResponse
from dcs_api_client.models.file_response import FileResponse
from dcs_api_client.models.gpg_key import GPGKey
from dcs_api_client.models.gpg_key_email import GPGKeyEmail
from dcs_api_client.models.general_api_settings import GeneralAPISettings
from dcs_api_client.models.general_attachment_settings import GeneralAttachmentSettings
from dcs_api_client.models.general_repo_settings import GeneralRepoSettings
from dcs_api_client.models.general_ui_settings import GeneralUISettings
from dcs_api_client.models.generate_repo_option import GenerateRepoOption
from dcs_api_client.models.git_blob_response import GitBlobResponse
from dcs_api_client.models.git_entry import GitEntry
from dcs_api_client.models.git_hook import GitHook
from dcs_api_client.models.git_object import GitObject
from dcs_api_client.models.git_service_type import GitServiceType
from dcs_api_client.models.git_tree_response import GitTreeResponse
from dcs_api_client.models.hook import Hook
from dcs_api_client.models.identity import Identity
from dcs_api_client.models.internal_tracker import InternalTracker
from dcs_api_client.models.issue import Issue
from dcs_api_client.models.issue_deadline import IssueDeadline
from dcs_api_client.models.issue_labels_option import IssueLabelsOption
from dcs_api_client.models.issue_template import IssueTemplate
from dcs_api_client.models.label import Label
from dcs_api_client.models.markdown_option import MarkdownOption
from dcs_api_client.models.merge_pull_request_option import MergePullRequestOption
from dcs_api_client.models.migrate_repo_form import MigrateRepoForm
from dcs_api_client.models.migrate_repo_options import MigrateRepoOptions
from dcs_api_client.models.milestone import Milestone
from dcs_api_client.models.notification_count import NotificationCount
from dcs_api_client.models.notification_subject import NotificationSubject
from dcs_api_client.models.notification_thread import NotificationThread
from dcs_api_client.models.notify_subject_type import NotifySubjectType
from dcs_api_client.models.o_auth2_application import OAuth2Application
from dcs_api_client.models.organization import Organization
from dcs_api_client.models.pr_branch_info import PRBranchInfo
from dcs_api_client.models.payload_commit import PayloadCommit
from dcs_api_client.models.payload_commit_verification import PayloadCommitVerification
from dcs_api_client.models.payload_user import PayloadUser
from dcs_api_client.models.permission import Permission
from dcs_api_client.models.public_key import PublicKey
from dcs_api_client.models.pull_request import PullRequest
from dcs_api_client.models.pull_request_meta import PullRequestMeta
from dcs_api_client.models.pull_review import PullReview
from dcs_api_client.models.pull_review_comment import PullReviewComment
from dcs_api_client.models.pull_review_request_options import PullReviewRequestOptions
from dcs_api_client.models.reaction import Reaction
from dcs_api_client.models.reference import Reference
from dcs_api_client.models.release import Release
from dcs_api_client.models.repo_commit import RepoCommit
from dcs_api_client.models.repo_topic_options import RepoTopicOptions
from dcs_api_client.models.repository import Repository
from dcs_api_client.models.repository_meta import RepositoryMeta
from dcs_api_client.models.review_state_type import ReviewStateType
from dcs_api_client.models.search_results import SearchResults
from dcs_api_client.models.server_version import ServerVersion
from dcs_api_client.models.state_type import StateType
from dcs_api_client.models.stop_watch import StopWatch
from dcs_api_client.models.submit_pull_review_options import SubmitPullReviewOptions
from dcs_api_client.models.tag import Tag
from dcs_api_client.models.team import Team
from dcs_api_client.models.time_stamp import TimeStamp
from dcs_api_client.models.topic_name import TopicName
from dcs_api_client.models.topic_response import TopicResponse
from dcs_api_client.models.tracked_time import TrackedTime
from dcs_api_client.models.transfer_repo_option import TransferRepoOption
from dcs_api_client.models.update_file_options import UpdateFileOptions
from dcs_api_client.models.user import User
from dcs_api_client.models.user_heatmap_data import UserHeatmapData
from dcs_api_client.models.user_settings import UserSettings
from dcs_api_client.models.user_settings_options import UserSettingsOptions
from dcs_api_client.models.watch_info import WatchInfo
